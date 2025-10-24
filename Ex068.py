from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if (total % 2 == 0 and tipo == 'P') or (total % 2 == 1 and tipo == 'I'):
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        break

print('=-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')

