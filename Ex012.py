preco = float(input('Qual é o preço do produto: R$'))
novo = preco - (0.05 * preco)

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar RS{novo:.2f}')