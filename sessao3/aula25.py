"""

interpolação basica de strings
s - string
d e i - int
f - float
x e X = hexadecimal (ABCDEF0123456789)


"""

# nome = 'lucas'
# preco = 1000.95897643
# variavel = '%s, o preço foi de R$%.2f' % (nome, preco)

# print(variavel)

# print('o hexadecimal de %d é  %04x' %(15, 15))

numero_hexa = input('qual vai ser o numero para conveter em hexadecimal? ')
numero_hexa = int(numero_hexa)

print(f'o numero {numero_hexa} em hexadecimal é {numero_hexa:04X}')