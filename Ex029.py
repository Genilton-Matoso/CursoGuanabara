velocidade = float(input('Digite a velocidade atual do carro ? '))

if velocidade <= 80:
    print('Tenha um bom dia! Voçê está no limite de velocidade permitido!')
else:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu a velocidade limite e vai pagar uma multa de R$ {multa})')