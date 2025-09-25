"""
flag(bandeira) - marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, indentidade)
id = indentidade

"""



condicao = False
passou_no_if = None

if condicao:
    print('faça algo')
    passou_no_if = True
else:
    print('não faça algo')

print(passou_no_if, passou_no_if is not None)
print(passou_no_if, passou_no_if is None)