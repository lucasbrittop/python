#lucas britto passarini RA: h334969
#declarando variaveis para o exercicio

nome = ...
numMultas = 0
maiorMulta = 0
NomeMaior = 0
valorMulta = 0
totalMulta = 0

while True: # laço infinito para adicionar motoristas
    nome = input("qual o nome do motorista? ")
    totalMulta = 0
    numMultas = 0
    while True:
        loop = input("deseja adicionar multa? (sim/não): ").lower() # pergunta para adicionar multas ou sair
        if "s" in loop:
            numMultas += 1
            valorMulta = int(input("qual o valor da multa? "))
            totalMulta += valorMulta
            if totalMulta > maiorMulta:
                maiorMulta = totalMulta
                NomeMaior = nome
        else:
            print("parou de adicionar multas")
            print(f"{nome} teve {numMultas} multas com o valor total em {totalMulta}")
            break
    continuar = input("deseja adicionar outro motorista? (sim/não): ").lower() # pergunta para adicionar outro motorista ou sair
    if "s" in continuar:
        continue
    else:
        print("parou de adicionar motoristas")
        break

print(f"a carteira com a multa mais alta foi para {NomeMaior} com o total de {maiorMulta} em multa(s)") # resultado final do motorista com maior multa