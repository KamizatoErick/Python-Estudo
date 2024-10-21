#isnumeric verifica se o que foi digitado é um número
#isspace verifica se é só espaço
#isalpha verifica se o que foi digitado é um alfabético/letra
#isalnum verifica se o que foi digitado é um alfabético/letra ou número
#isupper verifica se está somente com letrar maísculas
#islower verifica se está somente com letrar minúsculas
#istitle verifica se está começando com letra maiusculas e minúsculas


n = input('Informe algo: ')
print('O tipo primitivo desse valor é ', type(n))

print('É um número?', n.isnumeric())
print('Só tem espaços?', n.isspace())
print('É um alfabético?', n.isalpha())
print('É um alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())