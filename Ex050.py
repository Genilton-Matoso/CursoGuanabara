soma = 0
for i in range(1,7):
    num = int(input(f'Digite o {i} um valor: '))
    if num % 2 == 0 :
        soma += num
print(soma)
