numero = int(input('Digite um número inteiro: '))
binario = ''
print(bin(numero)[2:])
while numero > 0:
        binario += str((numero % 2))
        numero = numero // 2
print(binario[::-1])

