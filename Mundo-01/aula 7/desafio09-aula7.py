import os
def clear_terminal():
    # Verifica o sistema operacional e executa o comando apropriado
    os.system('cls' if os.name == 'nt' else 'clear')
# Chama a função para limpar o terminal
clear_terminal()

#######################################################

n1 = int(input('Digite um número: '))
contador = 1

print('\nTabuada do {}\n'.format(n1))

while True:
    print('{} x {} = {}'.format(n1, contador, n1*contador))
    contador += 1
    
    if(contador>10):
        break