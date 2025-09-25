"""
introdução ao try/except
try -> tenta executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('dobro do numero: ')


try:
    print(numero_str)
    numero_float = float(numero_str)
    print(numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um numero')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('isso não é um numero')