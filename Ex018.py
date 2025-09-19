import math
angulo = int(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tan:.2f}')