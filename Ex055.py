lista_peso = []
for i in range (1,6):
    peso = float(input(f'Peso da {i} pessoa: '))
    lista_peso.append(peso)
print(f'O maior peso lido foi de {max(lista_peso)}Kg')
print(f'O maior peso lido foi de {min(lista_peso)}Kg')