#lucas britto passarini RA: h334969
#declarando variaveis para o exercicio

contador = 0
soma = 0

while contador < 7: #repeticao para somar os 7 numeros
    num = input("digite o numero: ")
    
    try: #tratamento de erro caso o valor digitado não seja um numero
        num = int(num)
    except:
        print(f"o valor {num} é invalído")

    soma += num
    contador += 1

print(f"a soma de todos os 7 numeros é {soma}") #resultado final da soma dos 7 numeros