
texto = 'lucas britto'
novo_texto = ''
for i in texto:
    if i != ' ':
        novo_texto += i + '*'
    else:
        continue

print(novo_texto)