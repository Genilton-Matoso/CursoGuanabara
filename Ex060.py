#Fatorial calculando importnado a biblioteca
'''from math import factorial
n = int(input('digite o valor para calcular o fatorial: '))
fotorial = factorial(n)
print(fotorial)'''

n = int(input('digite o valor para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
