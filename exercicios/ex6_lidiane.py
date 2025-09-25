salario_bruto = input('qual o salario bruto? ')
salario_bruto = int(salario_bruto)

print(f'o salario é de {salario_bruto}')

valor_reajuste = salario_bruto * 0.38
salario_bruto = salario_bruto + valor_reajuste

print(f'o reajuste foi de {valor_reajuste} agora o salario é de {salario_bruto}')

valor_grati = salario_bruto * 0.2
salario_bruto = salario_bruto + valor_grati

print(f'com a gratificação, o salario foi para {salario_bruto}')

valor_inss = salario_bruto * 0.15
salario_bruto = salario_bruto - valor_inss

print(f'com o desconto do inss o salario final é de {salario_bruto}')
