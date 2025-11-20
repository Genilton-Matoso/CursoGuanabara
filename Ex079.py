lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')


