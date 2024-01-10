import requests

def obter_numero():
    while True:
        entrada = input("Qual opção deseja? ")
        
        try:
            # Tenta converter a entrada diretamente para float
            numero = float(entrada)
            break
        except ValueError:
            try:
                # Tenta converter a entrada com um único hífen para float
                numero = float(entrada.replace('-', '', 1))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    return entrada

api_url =  "https://parallelum.com.br/fipe/api/v1/carros/marcas"

response = requests.get(api_url)
# Convertendo a resposta para formato JSON (se a API retornar JSON)
data = response.json()

for marca in data:  
    #print(f'{dados}')
    resultado_formatado = ' '.join([f'{chave.upper()}: {valor}' for chave, valor in marca.items()])
    print(resultado_formatado)

#ESCOLHER MARCA
print()
m = obter_numero()
api_url =  f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{m}/modelos"

response = requests.get(api_url)
# Convertendo a resposta para formato JSON (se a API retornar JSON)
data = response.json()
modelos_lista = data.get('modelos', [])

print()
for modelo in modelos_lista:
    resultado_formatado = ' '.join([f'{chave.upper()}: {valor}' for chave, valor in modelo.items()])
    print(resultado_formatado)

#ESCOLHER MODELO
print()
carro = obter_numero()
api_url =  f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{m}/modelos/{carro}/anos"

response = requests.get(api_url)
# Convertendo a resposta para formato JSON (se a API retornar JSON)
data = response.json()
print()
for ano in data:  
    resultado_formatado = ' '.join([f'{chave.upper()}: {valor}' for chave, valor in ano.items()])
    print(resultado_formatado)

#ESCOLHER ANO
print()
anos = obter_numero()
api_url =  f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{m}/modelos/{carro}/anos/{anos}"

response = requests.get(api_url)
# Convertendo a resposta para formato JSON (se a API retornar JSON)
data = response.json()
print()
resultado_formatado = ' '.join([f'\n{chave.upper()}: {valor}' for chave, valor in data.items()])
print(resultado_formatado)