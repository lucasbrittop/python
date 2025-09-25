#operador logico 'not'
#usado para inverter expressões
# not true = false
# not false = true


print(not False)
print(not True)

senha = input('senha: ')

if not senha:
    print('sem senha')