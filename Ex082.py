lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
#for i, v in enumerate(lista): Esse metodo é para verificar o i indice e v valor
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de par {par}')
print(f'A lista de impar {impar}')