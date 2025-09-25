# operadores logicos
# and (e) or (ou) not (não)
#or - qualquer condição verdadeira = True (se uma das duas forem verdadeira = true)

# entrada = input('[E]ntrar e [S]air: ')
# senha_digitada = input('qual a senha do usuario? ')

# senha_permitida = '123456'


# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('entrar')
# else:
#     print('Sair')

#avaliação de curto circuito

senha = input('senha: ') or 'sem senha'
print(senha)