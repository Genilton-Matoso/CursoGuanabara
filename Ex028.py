from random import randint
from time import sleep

numero_computador = randint(0,5)

numero_usuario = int(input('Chute um numero entre 0 e 5: '))
print('Processando...')
sleep(2)
if numero_computador == numero_usuario:
    print('Parabéns... Voce acertou!')

else:
    print(f'Voce errou! Eu pensei no número {numero_computador}')


