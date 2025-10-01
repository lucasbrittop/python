import os




palavraSecreta = "azeitona"
palavraLetra = " "
contador = 1


while True:
    
    letra = input(f'#{contador} - adivinhe a palavra, fale uma letra: ')

    if letra.__len__() != 1:
        print("\n! apenas uma letra de cada vez !\n")
        continue

    palavraFormatada = ""

    if letra in palavraSecreta:
        if letra not in palavraLetra: 
            print(f'"{letra}" está na palavra') 
            palavraLetra += letra
    else:
        print(f'"{letra}" não está na palavra')

    for i in palavraSecreta:
        if i in palavraLetra:
            palavraFormatada += i
        else:
            palavraFormatada += '*'
    
    print('\n', palavraFormatada, '\n')
    

    contador += 1

    if palavraFormatada == palavraSecreta:
        os.system('cls')
        break



print('\nvoce ganhou meu amor te amo muito beiojos <3')

