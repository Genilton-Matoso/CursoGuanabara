distancia = float(input('Qual a distância da sua viagem? '))
print(f'Voçê está prestes a começar uma viagem de {distancia} Kn')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da sua viagem custara R$ {preco:.2f}')
