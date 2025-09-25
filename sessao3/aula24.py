# operadores in e not in
# strings são interaveis
# 0 1 2 3 4 5
# l u c a s
# -6-5-4-3-2-1

# nome = 'lucas'
# # print(nome[2])
# # print(nome[-3])

# print('z' in nome)
# print('a' in nome)
# print('z' not in nome)

nome = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print('tem')
else:
    print('não tem')