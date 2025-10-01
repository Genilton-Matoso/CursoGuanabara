A = float(input('Digite o primeiro valor: '))
B = float(input('Digite o segundo valor: '))
C = float(input('Digite o terceiro valor: '))

if A + B > C and A + C > B and B + C > A:
    print('O valores informados PODEM FORMAR um Triangulo')
    if A == B == C:
        print('O triangulo é EQUILÁTERO')
    elif A != B and B != C and A != C:
        print('O triangulo é ESCALENO')
    else:
        print('O triangulo é ISÓSCELES')
else:
    print('O valores informados NÃO podem formar um Triangulo')