somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range (1,5):
    print('-'*5 + f' {i}ª PESSOA' + '-'*5)
    nome = str(input('NOME: ')).strip()

    while True:
        try:
            idade = int(input('IDADE: '))
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")

    while True:
        try:
            sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
            if sexo == 'M' or sexo == 'F':
                break
        except ValueError:
            print("Por favor, digite um opção valida ")
    somaidade += idade
    if i == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho} ')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')


'''OUTRA FORMA COM LISTA

pessoas = []  # Cada pessoa será [nome, idade, sexo]

for i in range(1, 5):
    print('-'*5 + f' {i}ª PESSOA ' + '-'*5)
    
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]: ').strip().upper()[0]
    
    pessoas.append([nome, idade, sexo])

# Média de idade
mediaidade = sum(p[1] for p in pessoas) / len(pessoas)

# Homem mais velho
homens = [p for p in pessoas if p[2] == 'M']
if homens:
    homem_velho = max(homens, key=lambda x: x[1])
    nomevelho = homem_velho[0]
    idadevelho = homem_velho[1]
else:
    nomevelho = ''
    idadevelho = 0

# Mulheres com menos de 20 anos
totmulher20 = len([p for p in pessoas if p[2] == 'F' and p[1] < 20])

print(f'\nA média de idade do grupo é de {mediaidade:.1f} anos')
print(f'O homem mais velho tem {idadevelho} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')'''