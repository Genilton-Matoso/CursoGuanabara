A = float(input('Digite o primeiro valor: '))
B = float(input('Digite o segundo valor: '))
C = float(input('Digite o terceiro valor: '))

if A + B > C and A + C > B and B + C > A:
    print('O valores informados formam um Triangulo')
else:
    print('O valores informados NÃO formam um Triangulo')
