from  random import randint
computador = randint (1,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que cocê consegue adivinhar qual foi?''')
palpite = 0
tentativas = 0
while computador != palpite:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite > computador:
        print('Menos... Tente outra vez')
    elif palpite < computador:
        print('Mais... Tente outra vez')
print(f'Acertou com {tentativas} tentativas. Parabens!')
