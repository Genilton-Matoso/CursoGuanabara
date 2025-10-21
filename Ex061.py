print(30*'=')
print('10 TERMOS DE UMA PA')
print(30*'=')

p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += r
    cont += 1
print('FIM')
