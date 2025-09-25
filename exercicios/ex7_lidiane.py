while True:
    num = input('qual o numero? ')
    temp_num = num

    try:
        num = int(num)
    except:
        print('apenas numeros INTEIROS')
        continue
        
    soma = num - 1

    while soma:
        num = soma * num
        soma = soma - 1
    print(f'{temp_num}! é igual a {num}')

 




