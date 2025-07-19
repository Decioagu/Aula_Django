from reportlab.pdfgen import canvas
from pathlib import Path

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

# Cria o PDF e define o nome do arquivo
c = canvas.Canvas(f"{caminho_do_arquivo}/teste_01.pdf")

# Adiciona texto no PDF
c.drawString(100, 750, "Olá, este é um PDF gerado pelo ReportLab!")

# Salva o arquivo
c.save()



