import geoip2.database
from pathlib import Path

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

# Caminho para o arquivo GeoLite2-City.mmdb
db_path = caminho_do_arquivo / "GeoLite2-City.mmdb"

print(db_path)

# IP que você quer consultar
# ip_address = '8.8.8.8'  # Exemplo: Google DNS
ip_address = '0.0.0.0'  # Exemplo: Não existe

# Abrir o banco de dados GeoLite2
with geoip2.database.Reader(db_path) as reader:
    try:
        response = reader.city(ip_address)
        
        print(f"IP: {ip_address}")
        print(f"Cidade: {response.city.name}")
        print(f"Região: {response.subdivisions.most_specific.name}")
        print(f"País: {response.country.name}")
        print(f"Latitude: {response.location.latitude}")
        print(f"Longitude: {response.location.longitude}")
    except geoip2.errors.AddressNotFoundError:
        print(f"IP {ip_address} não encontrado no banco de dados.")

'''
O que é geoip2.database?
O módulo geoip2.database fornece a classe Reader, que permite abrir e 
consultar arquivos de banco de dados GeoIP (no formato .mmdb).

Esses arquivos contêm informações de geolocalização associadas a endereços IP. 
A biblioteca lê o arquivo e retorna dados como:
    - país 🌎
    - cidade 🏙️
    - latitude/longitude 📍
    - provedor de internet (ISP) 
'''