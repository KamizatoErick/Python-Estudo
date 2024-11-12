# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com parênteses
# abertos e fechados na ordem correta.
# Exemplo: ((a+c)*c

abriu = 0
fechou = 0

expressao = str(input('Digite a expressão: '))

for cont in range(0, len(expressao)):
    if '(' in expressao[cont]:
        abriu += 1
    if ')' in expressao[cont]:
        fechou += 1
    
if abriu == fechou:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')