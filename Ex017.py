from math import sqrt,hypot
co = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, adj) # calculo da hipotenusa
#hip = sqrt(pow(co, 2) + pow(adj, 2)) ou hip = sqrt(co**2 + adj**2) ou (co**2 + adj**2) * (0.5)
print(f'A hipotenusa vai medir {hip:.2f} ')
