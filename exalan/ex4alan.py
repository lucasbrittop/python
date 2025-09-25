#lucas britto passarini RA: h334969
#declarando variaveis para o exercicio

pct = 0
nome = ...
salario = 0
horas = 0
cont = 0

while cont < 5: # laço para 5 funcionarios
    nome = input("qual o nome do funcionario? ")
    salario = input("qual o salrio desse funcionario por dia? ")
    horas = input("quantas horas esse funcionario trabalhou no dia? ")

    try: #tratamento de erro caso algum valor digitado seja invalído
        nome = str(nome)
        salario = int(salario)
        horas = int(horas)
    except:
        print("algum argumento invalido")

    if horas < 10: #verificação de horas trabalhadas e calculo do salario
        print(f"o funcionario {nome} trabalhou por {horas} horas no dia e ganhou {salario}")
    elif horas >= 10 and horas < 12:
        pct = salario * 0.2
        salario = salario + pct
        print(f"o funcionario {nome} trabalhou por {horas} horas no dia e ganhou {salario}")
    elif horas >= 12:
        pct = salario * 0.3
        salario += pct
        print(f"o funcionario {nome} trabalhou por {horas} horas no dia e ganhou {salario}")

    cont -= 1 #contador para o laço
