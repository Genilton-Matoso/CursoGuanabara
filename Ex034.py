salario = float(input('Qual o salário do funcionário ? R$'))

if salario >= 1250:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f}')