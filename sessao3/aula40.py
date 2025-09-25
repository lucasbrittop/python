import os
""" calculadora while """

while True:

    num1 = input('qual primeiro numero? ')
    num2 = input('qual segundo numero? ')

    try:
        num1 = float(num1) 
        num2 = float(num2)
        os.system('cls')
    except:
        os.system('cls')
        print('apenas numeros'.upper())
        continue

    print(f'numeros escolhidos \n {num1} \n {num2}')
    print('\n 1 - soma \n 2 - subtração \n 3 - multiplicação \n 4 - divisão')
    op = input('\nqual a operação? ')
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = ...

    if num2 == 0:
        ...
    else:
        divisao = num1 / num2


    if op == '1':
        os.system('cls')
        print('resultado', soma)
    elif op == '2':
        os.system('cls')
        print('resultado', subtracao)
    elif op == '3':
        os.system('cls')
        print('resultado', multiplicacao)
    elif op == '4':
        if num2 == 0:
            os.system('cls')
            print('erro, divisão por zero')
            continue
        else:
            os.system('cls')
            print('resultado', divisao)
    else:
        os.system('cls')
        print('operação invalida')
        
    print('\n')
    sair = input('deseja calcular novamente? (sim/não)\n').lower()
    if 's' in sair:
        os.system('cls')
        continue
    else:
        os.system('cls')
        print('saiu')
        break

