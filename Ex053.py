frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')

frase_invertida = frase[::-1].upper().strip().replace(' ', '')

print(f'O inverso de {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')