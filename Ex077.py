tupla = ('APRENDER','PROGRAMAR','lINGUAGEM',
         'PYTHON','CURSO','GRATIS','ESTUDAR',
         'PRATICAR','TRABALHAR','MERCADO',
         'PROGRAMADOR','FUTURO')

for p in tupla:
    print(f'\nNa palavra {p} temos', end=' ' )
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')