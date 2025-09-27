from datetime import date

atual = date.today().year #calcula o ano atualmente

nascimento = int(input('Digite o ano de nascimento: '))

idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    ano = nascimento + 18
    print(f'você ainda não tem 18 anos faltam {saldo} anos para o alistamento!')
    print(f'Seu alistamento será em {ano} ano')
else:
    saldo = idade - 18
    ano = nascimento + 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    print(f'Seu alistamento foi em {ano} ano')

