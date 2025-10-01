import os

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    escolha = input("o que vc deseja fazer? \n 1 - adicionar valor \n 2 - remover valor \n 3 - ver lista \n : ")
    os.system('cls')

    if escolha == '1':
        try:
            valor = int(input('qual valor você quer adicionar? '))
            lista.append(valor)
        except:
            os.system('cls')
            print('apenas numeros inteiros')
            continue
    elif escolha == '2':
        if len(lista) != 0:
            print('lista de indices e seus valores: ')
            for indice, item in enumerate(lista):
                print(f'indice: {indice} | valor: {valor}')
            print('\n')
        else:
            print('nada a listar\n')
            continue
        
        try:
            valor = int(input('qual o indice do valor você quer remover? '))
        except:
            os.system('cls')
            print('isso não é um valor inteiro\n')
            continue

        try:
            print('valor removido: ', lista[valor])
            lista.pop(valor)    
        except:
            os.system('cls')
            print('indice não encontrado\n')
            continue

    elif escolha == '3':
        if len(lista) != 0:
            print('lista de indices e seus valores: ')
            for indice, item in enumerate(lista):
                print(f'indice: {indice} | valor: {item}')
            print('\n')
        else:
            print('nada a listar\n')
    else:
        os.system('cls')
        print('escolha não disponivel\n')
        continue
