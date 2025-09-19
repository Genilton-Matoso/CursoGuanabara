from math import sqrt

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = sqrt(n)
rz = n**(1/2)

print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}.')
print(f'A raiz quadrada de {n} importando math sqrt é vale {r:.2f}.')
print(f'A raiz quadrada de {n} sem importar é {rz:.2f}.')