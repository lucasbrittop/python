#lucas britto passarini RA: h334969
#declarando variaveis para o exercesse participante


nome = ...
idade = ...
peso = ...
contadorMais80 = 0
contadorMenos80 = 0
mediaMais80 = 0
mediaMenos80 = 0

while True: # laço infinito para adicionar participantes
    nome = input("qual o nome? ")
    idade = int(input("qual a idade? "))
    peso = float(input("qual o peso? "))
    
    if idade >= 20 and idade <= 30: # if para peso e idade permitida
        if peso >= 80:
            print("esse participante está na categoria com mais de 80kg")
            mediaMais80 = idade
            contadorMais80 += 1
        else:
            print("esse participante esta na categoiria com menos de 80kg")
            mediaMenos80 = idade
            contadorMenos80 += 1
    else:
        print("sua idade não é permitida")

    loop = input("deseja cadastrar outro participante? (sim/não): ").lower() # pergunta para cadastrar ou sair
    if "n" in loop:
        print("você escolheu sair")
        break
    else:
        print("você escolheu continuar")
        continue

if contadorMais80 != 0 and contadorMenos80 != 0: # if para verificar se as duas categorias tem participantes e mostrar a média
    print(f"a média das idades da categoria com menos de 80kg é {mediaMenos80 / contadorMenos80}")
    print(f"a média das idades da categoria com mais de 80kg é {mediaMais80 / contadorMais80}")
elif contadorMenos80 == 0: # if para verificar se uma das categorias não tem participantes e mostrar a média da outra
    print("a categoria menos de 80kg não tem participantes")
    print(f"a média das idades da categoria com mais de 80kg é {mediaMais80 / contadorMais80}")
elif contadorMais80 == 0: # if para verificar se uma das categorias não tem participantes e mostrar a média da outra
    print(f"a média das idades da categoria com menos de 80kg é {mediaMenos80 / contadorMenos80}")
    print("a categoria com mais de 80 não tem participantes")