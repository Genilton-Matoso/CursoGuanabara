lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*30)
print(f'você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO foi encontrado dentro da lista')