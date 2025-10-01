"""
enumetate - enumera interaveis (indices)
"""

lista = ['lucas', 'gabi', 'lola']
lista.append('cintia')

lista_enumerada = enumerate(lista)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)



for indice, nome in enumerate(lista):
    print(indice)