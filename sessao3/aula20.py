# tipo_comp = input('digite 1 para comparar numeros e 2 para palavras/letras ')
# valor_1 = ...
# valor_2 = ...

# if tipo_comp == '1':
#     print('você escolheu numeros')
#     valor_1 = int(input('qual valor 1? '))
#     valor_2 = int(input('qual valor 2? '))
# elif tipo_comp == '2':
#     print('você escolheu letras/palavras ')
#     valor_1 = input('qual valor 1? ')
#     valor_2 = input('qual valor 2? ')
# else:
#     print('opção inválida')



# if valor_1 > valor_2:
#     print(f"o valor 1 '{valor_1}' é maior que o valor 2 '{valor_2}'")
# elif valor_1 < valor_2:
#     print(f"o valor 1 '{valor_1}' é menor que o valor 2 '{valor_2}'")
# else:
#     print(f"o valor 1 '{valor_1}' é iguakl ao valor 2 '{valor_2}'")


valor_1 = input('qual o primeiro numero que vc quer comparar? ')
valor_2 = input('qual o segundo numero que vc quer comparar? ')

try:
    valor_1 = float(valor_1)
    valor_2 = float(valor_2)
    if valor_1 > valor_2:
        print(f"o valor 1 '{valor_1}' é maior que o valor 2 '{valor_2}'")
    elif valor_1 < valor_2:
        print(f"o valor 1 '{valor_1}' é menor que o valor 2 '{valor_2}'")
    else:
        print(f"o valor 1 '{valor_1}' é iguakl ao valor 2 '{valor_2}'")
except:
    print('isso não são numeros')
