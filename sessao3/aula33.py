#ex1

# numero_int = input('digite o numero inteiro: ')

# try:
#     numero_int = int(numero_int)
#     print(f'prosseguir, numero escolhido {numero_int}')
# except:
#     print('isso não é um numero inteiro')

# if numero_int % 2 == 0:
#     print(f'{numero_int} é par')
# else:
#     print(f'{numero_int} é impar')


# print('-' * 10)

#ex2

# hora = input('qual a hora? ')

# try:
#     hora = int(hora)
#     if hora <= 11:
#         print('bom dia')
#     elif hora <= 17:
#         print('boa tarde')
#     elif hora <= 23:
#         print('boa noite')
#     elif hora < 0:
#         print('horario invalido')
#     elif hora >= 24:
#         print('horario invalido')

# except:
#     print('isso não é uma hora')

#ex3 

primeiro_nome = input('digite seu primeiro nome: ')

primeiro_nome = len(primeiro_nome)

if primeiro_nome == 0:
    print('por favor, digite algo')
elif primeiro_nome <= 4:
    print('seu nome é curto')
elif primeiro_nome == 5 or primeiro_nome == 6:
    print('seu nome é medio')
elif primeiro_nome > 6:
    print('seu nome é grande')



