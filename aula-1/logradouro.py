import requests

# Joao Mateus Alves Costa Nunes de Barros
def logradouro2(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        logradouro = f"{dados['logradouro']}; {dados['complemento']}; {dados['bairro']}; {dados['localidade']}; {dados['uf']}"
        return logradouro
    else:
        return 'CEP não encontrado'

# Vinicius Camargo Mota Morici
def logradouro(cep):
    requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if requisicao.status_code != 200: return 'CEP não encontrado'
    json = requisicao.json()
    formatacao = f'{json["logradouro"]}; {json["complemento"]}; {json["bairro"]}; {json["localidade"]}; {json["uf"]}'
    return formatacao

print(logradouro('01133000'))
print(logradouro('01001000'))
print(logradouro('04013002'))
print(logradouro('abacaxi'))

cep = input('Digite o CEP desejado: ')
print(logradouro(cep))