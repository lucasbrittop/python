frase = 'meu nome é lucas brittto'
frase = frase.lower()
mais_vezes = 0
letra_mais = ""


i = 0
while i < len(frase):
    
    letra_atual = frase[i]
    vezes = frase.count(letra_atual)
    i += 1
    if letra_atual == " ":
        continue

    if vezes > mais_vezes:
        mais_vezes = vezes
        letra_mais = letra_atual

    

print(letra_mais, mais_vezes)