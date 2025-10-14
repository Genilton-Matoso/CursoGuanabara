s = 0
n = 0
for i in range(1,501,2):
    if i % 3 == 0:
        s += i
        n += 1
print(f'O total de numero divisíveis por 3 são {n} e sua soma é: {s}')