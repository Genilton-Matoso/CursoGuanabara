times = ('Corinthians','Palmeiras','santos','Grêmio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia',
         'São Paulo','Fluminense','Sport Recife',
         'EC Vitoria','Coritiba','Avaí','Ponte Preta',
         'Atlético-GO')

print('-='*20)
print(f'Lista de times do Brasileirão {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)} ')
print('-='*20)
print(f'O chapecoense está na {times.index('Chapecoense')+1}ª posição')

