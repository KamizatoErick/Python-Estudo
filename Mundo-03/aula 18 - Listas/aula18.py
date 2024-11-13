# Este arquivo é somente para anotações sobre Listas

galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]

for p in galera:
    print(p)

for p in galera:
    print(f'O nome {p[0]} tem {p[1]} anos de idade.')

print('=-'*30)

galera2 = []
dado = []
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

    galera2.append(dado[:]) # Cria uma cópia
    dado.clear()
print(galera2)

for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')