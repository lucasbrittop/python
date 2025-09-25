nome_usuario = input('digite seu nome: ')
idade_usuario = input('digite sua idade: ')


if nome_usuario and idade_usuario:
    print(f'seu nome é {nome_usuario}')
    print(f'seu nome invertido é {nome_usuario[::-1]}')
    if ' ' in nome_usuario:
        print(f'{nome_usuario} tem espaços')
    else:
        print(f'{nome_usuario} não tem espaços')
    print(f'o seu nome tem {len(nome_usuario)} letras')
    print(f'a primeira letra do nome {nome_usuario} é {nome_usuario[0]}')
    print(f'a ultima letra do nome {nome_usuario} é {nome_usuario[-1]}')
elif nome_usuario and True:
    print('campo de idade não escrito')
elif idade_usuario and True:
    print('campo de nome não escrito')
else:
    print('nenhum campo esrito')