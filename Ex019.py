from random import choice
p1 = input('Primeiro aluno: ')
p2 = input('Segundo aluno: ')
p3 = input('Terceiro aluno: ')
p4 = input('Quarto aluno: ')

alunos = [p1, p2, p3, p4]
escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}')