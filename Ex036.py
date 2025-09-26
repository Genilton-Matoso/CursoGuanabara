casa = float(input('\033[33mValor da casa: R$' ))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${prestacao:.2f}')
if prestacao >= minimo:
    print('EMPRESTIMO NEGADO')
else:
    print('EMPRESTIMO ACEITO')

