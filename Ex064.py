n = 0
cont = 0
total = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    total += n
print(f'você digitou {cont} números e a soma entre eles foi {total}')

