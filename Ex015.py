d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = d * 60 + km * 0.15

print(f'O total a pagar é de R${valor:.2f}')

