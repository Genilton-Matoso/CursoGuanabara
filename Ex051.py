from pickletools import decimalnl_long

print(30*'=')
print('10 TERMOS DE UMA PA')
print(30*'=')

p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10-1) * r
for i in range(p,decimo + r,r):
    print(i, end=' ')
print('FIM')