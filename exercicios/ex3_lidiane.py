votos_brancos = input('votos brancos: ')
votos_validos = input('votos valídos: ')
votos_nulos = input('votos nulos: ')

votos_validos = int(votos_validos)
votos_brancos = int(votos_brancos)
votos_nulos = int(votos_nulos)


totais = votos_brancos + votos_nulos + votos_validos


votos_validos = (votos_validos / totais) * 100
votos_brancos =  (votos_brancos / totais) * 100
votos_nulos = (votos_nulos / totais) * 100

print(f'os votos totais são {totais}')
print(f'os votos brancos são {votos_brancos:.2f}%')
print(f'os votos nulos são {votos_nulos:.2f}%')
print(f'os votos valídos são {votos_validos:.2f}%')