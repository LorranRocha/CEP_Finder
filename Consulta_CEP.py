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

def main():
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

    opcao = int(input("Deseja realizar outra consulta?\n1 - Sim\n2 - Não\n\nR:"))

    if opcao == 1:
        main()
    else:
        limpar()
        print("Obrigado por usar nosso sistema!!!")
        time.sleep(2)
        exit()

if __name__ == '__main__':
    main()