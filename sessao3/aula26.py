"""
formatação basica de strings
s - string
d - int
f - float
. <numero de digitos> f
x ou X - hexadecimal
(caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
= força o numero a aparecer antes dos zeros
sinal - + ou -
ex.: 0>-100,.1f
conversion flags -  !r !s !a
"""

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{variavel: <10}')
print(f'{1000.17824617461:0>+10,.1f}')
print(f'1500 em hexa é {1500:08x}')
print(f'{variavel!r}')