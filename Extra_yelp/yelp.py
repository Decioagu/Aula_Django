import requests
from dotenv import load_dotenv 
import os

load_dotenv()

CHAVE = os.getenv('chave')

# 🔑 Defina sua chave do Yelp aqui
YELP_API_KEY = CHAVE # Sucesso
# YELP_API_KEY = 'aaa' # Erro

# 🌐 Endpoint do Yelp
YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

def yelp_search(keyword=None, location=None):
    headers = {"Authorization": "Bearer " + YELP_API_KEY}
    params = {'term': keyword, 'location': location}

    response = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    if response.status_code == 200:
        # Sucesso: retorna o JSON
        return response.json()
    else:
        # Erro: mostra o código e resposta
        print(f"Erro {response.status_code}: {response.text}")
        return None


# 🧪 Teste a busca
if __name__ == "__main__":
    resultado = yelp_search("Pizzaria", "Rio de Janeiro")

    if resultado:
        for negocio in resultado.get("businesses", []):
            print(f"- {negocio['name']} ({negocio['location']['address1']})")

'''
O que é o Yelp?
    - https://www.yelp.com.br/rio-de-janeiro
    
O Yelp é uma plataforma online (site e aplicativo) onde pessoas podem:
✅ - Procurar empresas locais (restaurantes, bares, academias, lojas, etc.)
✅ - Verificar avaliações e notas deixadas por outros usuários
✅ - Consultar informações como telefone, endereço, fotos, horário de funcionamento e até fazer reservas.

O Yelp tem uma API chamada Yelp Fusion API, que oferece vários endpoints para diferentes funcionalidades, por exemplo:
URL da API do Yelp para buscar empresas por palavra-chave (term) e localização (location).

https://www.yelp.com/developers/v3/manage_app
'''