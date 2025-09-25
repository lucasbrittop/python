"""
repetição
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> qaundo o código não tem fim
"""

qnt_linhas = 5
qnt_colunas = 5

linha = 1

while linha <= qnt_linhas:
    coluna = 1
    while coluna <= qnt_colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
print('acabou')