from weasyprint import HTML

html = """
<html>
  <body>
    <h1 style="color:blue;">Olá WeasyPrint!</h1>
  </body>
</html>
"""

HTML(string=html).write_pdf("teste.pdf")
print("✅ PDF gerado com sucesso!")
