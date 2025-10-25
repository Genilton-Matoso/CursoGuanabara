total = totalmil = menor = 0
barato = ''

print('_'*30)
print('      LOJA SUPER BARATÃO')
print('_'*30)
while True:
    produto = str(input('Nome do produto?: '))
    preco = float(input('Preço: '))
    total += preco

    if preco > 1000:
        totalmil += 1

    if menor == 0 or preco < menor:
        menor = preco
        barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O valor total da compra foi R$ {total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor}')

