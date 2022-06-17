#   Using Python 3.10.5
#   pip install requests
#   Author: Lorran Rocha dos Santos (https://www.lorranrocha.com/)
#   Api url : https://viacep.com.br/


import requests
import os
import time


def limpar():
    try:
        os.system('clear')
    finally:
        os.system('cls')
    
limpar()

print("Bem Vindo ao Consulta CEP!")

time.sleep(4)

limpar()


cep = input("Digite o CEP desejado: ")


if len(cep) != 8:
    limpar()
    print("O CEP {} é inválido! \nFavor inserir outro!".format(cep))
    time.sleep(2)
    
    exit()

api = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

dados = api.json()

if 'erro' not in dados:
    limpar()
    print("OPA! CEP ENCONTRADO!!!!\n")
    print("CEP: {}".format(dados['cep']))
    print("Logradouro: {}".format(dados['logradouro']))
    print("Bairro: {}".format(dados['bairro']))
    print("Cidade: {}".format(dados['localidade']))
    print("Estado: {}".format(dados['uf']))
    print("\nCriado por: https://www.lorranrocha.com/\n")

else:
    limpar()
    print("OPA! CEP NÃO ENCONTRADO!!!!\n")

