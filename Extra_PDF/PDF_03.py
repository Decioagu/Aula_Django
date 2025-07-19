from weasyprint import HTML
from pathlib import Path

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

html = """
<html>
  <body>
    <h1 style="color:blue;">Olá WeasyPrint!</h1>
  </body>
</html>
"""

HTML(string=html).write_pdf(f"{caminho_do_arquivo }/teste_03.pdf")
print("✅ PDF gerado com sucesso!")
