"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'abcde' # 5 caracteres

lista = [123, True, 'lucas britto', 1.2]

print(bool(lista)) # vazia -> falso

#print(lista, type(lista))

lista[2] = 'gabi'
print(lista[2])


listaNum = [1, 2, 3, 4]

# del listaNum[2]

# print(listaNum)

listaNum.append('felipe neto')

print(listaNum)

listaNum.pop()
listaNum.pop(0)
ultimo_valor = listaNum.pop()
listaNum.insert(0, 10) #adiciona um valor no indice escolhido

print(listaNum, ultimo_valor)

listaA = [1,2,3]
listaB = [4,5,6]

listaC = listaA + listaB
listaD = listaA.extend(listaB)
print(listaC)
print(listaA)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista01 = ['lucas', 'gabi']
lista02 = lista01.copy()

lista01.append('oi')
print(lista02)
print(lista01)