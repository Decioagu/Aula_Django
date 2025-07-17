import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2

#23 Definindo a URL da API
YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search' 

#23 Busca no "Yelp" por palavra chave e localização
def yelp_search(keyword=None, location=None): 
    #23 Definindo a chave da API
    headers = {"Authorization": "Bearer " + settings.YELP_API_KEY} 

    #23 Se houver palavra chave e localização
    if keyword and location: 
        #23 Palavra chave e localização
        params = {'term': keyword, 'location': location}

    try:
        #23 Fazendo a busca
        print(f'Buscando no Yelp no site "{YELP_SEARCH_ENDPOINT}"')
        print(f'parâmetros "{params.values()}"')
        r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params) 
                    #(       SITE        ,chave autorização, parâmetros da busca)
        return r.json() #23 Retorno da busca
    except Exception as e:
        # Tratar erro (API não encontrada)
        print(f"Erro ao buscar cidade para o IP: {e}")
        return None


#23 Busca no "GeoIP2" (Simula IP de localização de onde o usuário esta pesquisando)
def get_client_data():
    geoip = GeoIP2() #23 Instancia o GeoIP2
    ip = get_random_ip() #23 Gera um IP ALEATÓRIO  ex: '144.221.131.251'
    try:
        return geoip.city(ip) #23 Busca GeoIP2().cidade(IP ALEATÓRIO)
    except Exception as e:
        # Tratar erro (IP ALEATÓRIO não encontrado)
        print(f"Erro ao buscar cidade para o IP: {e}")
        return None

#23 "Função auxiliar" para gera um IP ALEATÓRIO
def get_random_ip(): 
    return '.'.join([str(randint(0, 255)) for x in range(4)]) # Ex: '144.221.131.251'

'''
Resumo da função geral do arquivo
    - Uso de integração com API do "Yelp" para buscar negócios locais com 
    base em palavra-chave e localização.

    - Uso do "GeoIP2" para geolocalização via IP, mas no código atual está usando IPs aleatórios 
    para testes, simula IP de localização de onde o usuário esta pesquisando.

    - "Função auxiliar" para obter dados de cidade via IP 
    (apesar de estar usando IPs aleatórios, que não refletem a localização real de usuários).

Observações
    Para realmente obter a localização do cliente, o ideal seria pegar o IP real do usuário 
    (por exemplo, do request HTTP) e usar esse IP em GeoIP2 para identificar a cidade.
    Usar IPs aleatórios pode ser só para teste ou demonstração.
    A API do Yelp precisa da chave correta configurada no settings.py para funcionar.
'''