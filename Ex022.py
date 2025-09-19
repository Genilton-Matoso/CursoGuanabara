nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
lista = nome.split()
print(len(lista[0]))

