from random import randint
from django.views.generic import TemplateView # Importa as views genéricas do Django
from chartjs.views.lines import BaseLineChartView # Importa a classe BaseLineChartView

#24 Classe de gerenciamento da página inicial
class IndexView(TemplateView):
    template_name = 'index.html'

#24 Classe de gerenciamento da página de dados
class DadosJSONView(BaseLineChartView):

    #24 Retorna 12 labels (colunas)
    def get_labels(self):
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    #24 Retorna os nomes das 6 datasets (linhas)
    def get_providers(self):
        datasets = [
            "Programação para Leigos",
            "Algoritmos e Lógica de Programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"
        ]
        return datasets

    #24 Retorna 6 datasets para plotar o gráfico
    def get_data(self):
        """
        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        6 datasets, então 6 linhas.
        12 labels, então 12 colunas.
        """
        dados = [] # lista

        for l in range(6): # 6 linhas
            for c in range(12): # 12 colunas

                # randint(min, max) |  número inteiro aleatório
                dado = [
                    randint(1, 100),  # jan
                    randint(1, 100),  # fev
                    randint(1, 100),  # mar
                    randint(1, 100),  # abr
                    randint(1, 100),  # mai
                    randint(1, 100),  # jun
                    randint(1, 100),  # jul
                    randint(1, 100),  # ago
                    randint(1, 100),  # set
                    randint(1, 100),  # out
                    randint(1, 100),  # nov
                    randint(1, 100)   # dez
                ]

            dados.append(dado) # adiciona na lista

        return dados

