import os
import asyncio
import time
import schedule
import pandas as pd
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import quote
from browser_use import Agent, Browser, ChatGoogle, ChatBrowserUse  # ← ChatGoogle para Gemini!

# === CONFIG ===
load_dotenv()

# Chave da API do Google Gemini
BROWSER_USE_API_KEY = os.getenv("GOOGLE_API_KEY")

#GOOGLE_API_KEY = "AIzaSyDs6pf0pzr-RlyiPgX5nDwEXnHvtEPJ9fE"

# === WHATSAPP ===
SEU_NUMERO = "5521999289987"

# === DADOS DA VIAGEM ===
DESTINO = "Petrópolis, RJ"
ORCAMENTO = 2000
# ← REMOVIDO O "b" SOLTO AQUI!

# === FUNÇÃO WHATSAPP ===
def enviar_whatsapp(msg):
    encoded_msg = quote(msg)
    whatsapp_link = f"https://wa.me/{SEU_NUMERO}?text={encoded_msg}"
    print("\n📲 Link do WhatsApp gerado:")
    print(whatsapp_link)
    try:
        webbrowser.open(whatsapp_link)
        print("🌐 Link aberto no navegador. Envie a mensagem manualmente.")
    except:
        print("⚠️ Não foi possível abrir o navegador. Copie e cole o link manualmente.")

# === AGENTE COM GEMINI ===
async def rodar_agente(tipo="manha"):
    browser = Browser(use_cloud=False, 
    headless=True,
    executable_path="/usr/local/bin/chromium",  
    timeout=60  # segundos para cada operação
    )
    
    
    # Usando Gemini diretamente do browser_use (sem LangChain!)
    # llm = ChatGoogle(model='gemini-3.0-flash', api_key=GOOGLE_API_KEY)  # [citation:1]
    # Initialize the model (defaults to bu-latest)
    llm = ChatBrowserUse()

    if tipo == "manha":
        tarefa = f"""
        Buscar preços atualizados de:
        - aluguel de carro em Niterói
        - pousadas em Petrópolis com café da manhã

        Retornar:
        - nome
        - preço
        - link
        """
    else:
        tarefa = f"""
        Analisar os dados coletados hoje e identificar:
        - melhor custo-benefício
        - se está dentro do orçamento de R$ {ORCAMENTO}
        """

    agent = Agent(task=tarefa, llm=llm, browser=browser)
    result = await agent.run()
    await browser.close()  # ← Fecha o navegador para liberar recursos
    return result

# === FUNÇÃO AUXILIAR PARA RODAR ASYNC DENTRO DO SCHEDULE ===
def rodar_async_com_novo_loop(tipo):
    """Cria um novo event loop para cada execução - resolve conflito com schedule"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        resultado = loop.run_until_complete(rodar_agente(tipo))
        return resultado
    finally:
        loop.close()

# === SALVAR HISTÓRICO ===
def salvar_historico(dados):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    result_str = str(dados) if dados else ""
    df = pd.DataFrame([{"data": data, "resultado": result_str}])

    try:
        df.to_csv("historico_viagem.csv", mode="a", header=False, index=False)
    except:
        df.to_csv("historico_viagem.csv", index=False)

# === JOB MANHÃ ===
def job_manha():
    print("🌅 Rodando tarefa da manhã...")
    resultado = rodar_async_com_novo_loop("manha")
    salvar_historico(resultado)
    markdown_msg = f"""# 🌅 Atualização da viagem - {datetime.now().strftime('%d/%m/%Y %H:%M')}

**Destino:** {DESTINO}  
**Orçamento:** R$ {ORCAMENTO}

## Resultados:
{resultado}
"""
    enviar_whatsapp(markdown_msg)

# === JOB NOITE ===
def job_noite():
    print("🌙 Rodando tarefa da noite...")
    resultado = rodar_async_com_novo_loop("noite")
    salvar_historico(resultado)
    markdown_msg = f"""# 🌙 Análise da viagem - {datetime.now().strftime('%d/%m/%Y %H:%M')}

**Destino:** {DESTINO}  
**Orçamento:** R$ {ORCAMENTO}

## Análise:
{resultado}
"""
    enviar_whatsapp(markdown_msg)

# === MAIN ===
def main():
    print("=== AGENTE DE VIAGEM ===")
    print("Escolha uma opção:")
    print("1. Rodar tarefa da manhã agora")
    print("2. Rodar tarefa da noite agora")
    print("3. Agendar automaticamente (8h e 20h)")
    opcao = input("Digite 1, 2 ou 3: ").strip()

    if opcao == "1":
        print("Executando tarefa da manhã...")
        job_manha()
        print("Concluído.")
    elif opcao == "2":
        print("Executando tarefa da noite...")
        job_noite()
        print("Concluído.")
    elif opcao == "3":
        print("🤖 Agendamento iniciado. As tarefas serão executadas às 8:00 e 20:00.")
        schedule.every().day.at("08:00").do(job_manha)
        schedule.every().day.at("20:00").do(job_noite)

        while True:
            schedule.run_pending()
            time.sleep(60)
    else:
        print("Opção inválida. Encerrando.")

if __name__ == "__main__":
    main()