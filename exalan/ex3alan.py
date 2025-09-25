#lucas britto passarini RA: h334969
#declarando variaveis para o exercicio

min = input("digite o minimo: ")
max = input("digite o maximo: ")

try: #tratamento de erro caso o valor digitado não seja um numero
    min = float(min)
    max = float(max)
except:
    print("argumento invalído")

contador = min
soma = 0

while contador < max: #laço para verificar se o numero é par ou impar e somar os pares
    if contador % 2 == 0:
        print(f"{contador} é par")
        soma = soma + contador

    contador += 1

print(f"a soma dos pares é {soma}") #resultado final da soma dos numeros pares

