from random import randint

numero_computador = randint(0,5)

numero_usuario = int(input('Chute um numero entre 0 e 5: '))

if numero_computador == numero_usuario:
    print('Voce acertou!')

else:
    print('Voce errou!!!')


