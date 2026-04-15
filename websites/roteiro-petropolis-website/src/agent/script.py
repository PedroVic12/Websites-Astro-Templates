import os
import asyncio
import time
import schedule
import pandas as pd
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import quote
from browser_use import Agent, Browser, ChatBrowserUse

# === CONFIG ===
load_dotenv()

API_KEY = os.getenv("API_KEY")

API_KEY = "bu_AgbHIeHO4ZW_o37ZIV56bL_mh6vhEHjfUHwr3zi88LY"

# === WHATSAPP ===
# Replace with your international phone number without plus sign, e.g., "5511999999999"
SEU_NUMERO = "5521999289987"  # Change to your actual number

# === DADOS DA VIAGEM ===
DESTINO = "Petrópolis, RJ"
ORCAMENTO = 2000


# === FUNÇÃO WHATSAPP (via link) ===
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


# === AGENTE ===
async def rodar_agente(tipo="manha"):
    browser = Browser(use_cloud=False, headless=False)
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
    return result


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
    resultado = asyncio.run(rodar_agente("manha"))
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
    resultado = asyncio.run(rodar_agente("noite"))
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
