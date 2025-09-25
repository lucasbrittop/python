#lucas britto passarini RA: h334969
#declarando variaveis para o exercicio

numContador = 0
maior = 0
menor = 0

while numContador < 10: #repeticao para verificar se é menor ou maior que 20
    num = input("digite o numero: ")
    
    try: #tratamento de erro caso o valor digitado não seja um numero
        num = int(num)
    except:
        print(f'o valor {num} é invalído')

    if num > 20: #verificação se é maior ou menor que 20
        maior += 1

    else:
        menor += 1

    
    numContador += 1

print(f'existem {maior} maiores que 20') #resultado final maior que 20
print(f'existem {menor} menores que 20') #resultado final menor que 20
