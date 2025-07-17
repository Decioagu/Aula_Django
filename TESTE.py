import geoip2.database

# Caminho para o arquivo GeoLite2-City.mmdb
db_path = "Aula_23/geoip/GeoLite2-City.mmdb"

# IP que você quer consultar
ip_address = '0.0.0.0'  # Exemplo: Google DNS

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
