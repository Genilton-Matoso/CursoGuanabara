from time import sleep

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} + {segundo} é {soma}')
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print(f'A multiplicação entre {primeiro} x {segundo} é {multiplicar}')
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f'Entre {primeiro} e {segundo} o maior é {maior} ')
    elif opcao == 4:
        print('Informe os números novos...')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando!')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')






