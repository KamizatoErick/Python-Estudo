# Para colocar letra, basta usar \033[m
# E entre [ e 'm' inserir o código das cores.
# Exemplo: \033[0;31;42m
# sendo 0 style, 31 texto e 42 back.

print('\033[0;31;42mOlá, Mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print('-='*14)

# Outra forma de aplicar cores
nome = 'Erick'
print('Olá, {}{}{}!'.format('\033[1;32m', nome, '\033[m'))

# Outra forma
cores = {'limpa':'\033[m', 
         'azul':'\033[34m',
         'amarelo':'\033[33m'}

print('Olá, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
