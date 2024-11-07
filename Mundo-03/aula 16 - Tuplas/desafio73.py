# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonado Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Vasco da Gama.

times = ('Bota Fogo','Palmeiras','Fortaleza','Internacional','Flamengo','São Paulo',
         'Bahia','Cruzeiro','Vasco da Gama','Atlético-MG','Grêmio','Vitória',
         'Corinthians','Fluminense','Criciúma','Bragantino','Athletico-PR',
         'Juventude','Cuiabá','Atlético-GO')

print('=-=-'*22)
print(f'Os 5 primeiros são {times[0:5]}')
print('=-=-'*22)
print(f'Os 4 últimos são {times[16:]}')
print('=-=-'*22)
print(f'Ordem Alfabética: {sorted(times)}')
print('=-=-'*22)
for c in range(0,len(times)):
    if times[c] == 'Vasco da Gama':
        print(f'O Vasco da Gama está na posição {c}')
        break