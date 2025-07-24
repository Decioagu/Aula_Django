import io
from django.http import FileResponse
from django.views.generic import View

from reportlab.pdfgen import canvas

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML


class IndexView(View):

    def get(self, request, *args, **kwargs):

        # Cria um arquivo em memória para receber os dados e gerar o PDF
        buffer = io.BytesIO() # Arquivo em memória

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer) # Arquivo com extensão .pdf

        # Insere 'coisas' no PDF
        pdf.drawString(50, 750, "Página 1: Décio Santana de Aguiar") # Insere um texto

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage() # Finaliza página 1 e cria página 2 em branco .pdf

         # Insere 'coisas' no PDF
        pdf.drawString(100, 100, "Página 2: Continuamos aqui!") # Insere um texto

        # Salva o PDF
        pdf.save() 

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0) # Vai para o início do arquivo em .pdf

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf') # Retorna o PDF
    
        ## Faz o download do arquivo em PDF gerado
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

import tempfile
import os
class Index2View(View):

    def get(self, request, *args, **kwargs):
        # lista de textos
        texto = ['Décio Santana de Aguiar', 'Programador Python', 'Programação Web com Python e Django']

        html_string = render_to_string('relatorio.html', {'texto': texto}) # Renderiza o HTML

        html = HTML(string=html_string) # Cria o HTML

        # Usa um caminho temporário seguro
        tmp_dir = tempfile.gettempdir() # Cria um caminho temporário
        tmp_path = os.path.join(tmp_dir, 'relatorio2.pdf') # Junta o caminho com o nome do arquivo
        html.write_pdf(target=tmp_path) # Gera o PDF

        # Lê o arquivo gerado no navegador
        with open(tmp_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf') # Retorna o PDF
            # Abre no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'

            ## Ou para forçar o download:
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

        return response