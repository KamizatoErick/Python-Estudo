import os
def clear_terminal():
    # Verifica o sistema operacional e executa o comando apropriado
    os.system('cls' if os.name == 'nt' else 'clear')
# Chama a função para limpar o terminal
clear_terminal()

#######################################################

n = input('Informe algo: ')
print('O tipo primitivo desse valor é ', type(n))

print('É um número?', n.isnumeric())
print('Só tem espaços?', n.isspace())
print('É um alfabético?', n.isalpha())
print('É um alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())