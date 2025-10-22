cont = 0
soma = 0
lista = []
resp = 'S'
media = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    lista.append(n)
    soma += n
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a media foi {media:.2f}')
print(f'O maior valor foi {max(lista)} e o menor foi {min(lista)}')