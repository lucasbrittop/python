"""
iteravel -> str, range, etc
interador -> quem sabe entregar um valor por vez
next -> me entrgue o próximo valor
inter -> me entregue um interador
"""
texto = "lucas" #itravel
iterador = iter(texto) #iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
