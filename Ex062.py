print(30*'=')
print('10 TERMOS DE UMA PA')
print(30*'=')

p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += r
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
