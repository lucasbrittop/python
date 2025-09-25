valor_total = input('valor total: ')
valor_total = int(valor_total)

# 10% saude
valor_saude = valor_total * 0.1
valor_total = valor_total - valor_saude
# 25% educação
valor_edu = valor_total * 0.25
valor_total = valor_total - valor_edu
# 30% alimentação
valor_ali = valor_total * 0.3
valor_total = valor_total - valor_ali
# 10% vestuario
valor_vest = valor_total * 0.1
valor_total = valor_total - valor_vest
# 5% lazer
valor_lazer = valor_total * 0.05
valor_total = valor_total - valor_lazer
# 20% outros
valor_outros = valor_total * 0.2
valor_total = valor_total - valor_outros

print(valor_total, valor_edu, valor_ali, valor_vest, valor_lazer, valor_outros)
print(valor_total + valor_edu + valor_ali + valor_vest + valor_lazer + valor_outros)