print('{:=^40}'.format(' PROGRAMA DE PROGRAMA '))
preco = float(input('Preço das compras: R$'))

print('''FORMA DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))


match opcao:
    case 1:
        valor_desconto = preco * 0.90

    case 2:
        valor_desconto = preco * 0.95

    case 3:
        valor = preco/2
        valor_desconto = preco
        print(f'Sua compra se será parcelada em 2x de R${valor:.2f} SEM JUROS')
    case 4:
        parcelas = int(input('Quantas parcelas? '))
        valor_desconto = preco * 1.20
        valor_parcelado = valor_desconto / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcelado:.2f} COM JUROS')
    case _:
        valor_desconto = preco
        print('Opção invalida!!')
print(f'Sua compra de R${preco:.2f} vai custar R${valor_desconto:.2f} no final')