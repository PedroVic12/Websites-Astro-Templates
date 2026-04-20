from fpdf import FPDF

# Criar objeto PDF
pdf = FPDF(unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# Titulo
pdf.cell(200, 10, "Roteiro Petropolis - Restaurantes Acessiveis", ln=True, align="C")
pdf.ln(10)

# Dados do roteiro
roteiro = [
    ("21/04", "11h30", "Almoco", "Duetto's Cafe & Bistrô", "R$50"),
    ("21/04", "13h00", "Museu Imperial", "", ""),
    ("21/04", "15h00", "Catedral Sao Pedro de Alcantara", "", ""),
    ("21/04", "19h30", "Jantar", "Trattoria do Filippi", "R$70"),
    ("22/04", "Manha", "Home Office", "", ""),
    ("22/04", "16h00", "Palacio de Cristal", "", ""),
    ("22/04", "20h00", "Jantar", "Casa do Alemao", "R$60"),
    ("23/04", "09h30", "Museu de Cera", "", ""),
    ("23/04", "12h00", "Almoco + Tour", "Cervejaria Bohemia", "R$80"),
    ("23/04", "14h30", "Casa de Santos Dumont", "", ""),
    ("23/04", "16h00", "Casa dos 7 Erros", "", ""),
    ("23/04", "19h30", "Jantar", "Petiscaria Lago Sul", "R$70"),
    ("24/04", "Manha", "Home Office", "", ""),
    ("24/04", "16h00", "Rua Teresa", "", ""),
    ("24/04", "19h00", "Cinema", "Cine Show Petropolis", "R$50"),
    ("24/04", "21h00", "Jantar", "Majorica (prato individual)", "R$70"),
    ("25/04", "08h30", "Cafe da manha", "Hotel Kastel (incluso)", "-"),
    ("25/04", "10h00", "Check-out e retorno", "", ""),
]

# Cabecalho da tabela
pdf.set_font("Helvetica", "B", 12)
pdf.cell(30, 10, "Data", 1)
pdf.cell(30, 10, "Horario", 1)
pdf.cell(70, 10, "Atividade/Passeio", 1)
pdf.cell(50, 10, "Restaurante", 1)
pdf.cell(20, 10, "Custo", 1)
pdf.ln()

# Conteudo da tabela
pdf.set_font("Helvetica", size=10)
for item in roteiro:
    pdf.cell(30, 10, item[0], 1)
    pdf.cell(30, 10, item[1], 1)
    pdf.cell(70, 10, item[2], 1)
    pdf.cell(50, 10, item[3], 1)
    pdf.cell(20, 10, item[4], 1)
    pdf.ln()

# Salvar PDF
pdf.output("roteiro_petropolis.pdf")
