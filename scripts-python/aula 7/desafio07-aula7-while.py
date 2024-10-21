import os
def clear_terminal():
    # Verifica o sistema operacional e executa o comando apropriado
    os.system('cls' if os.name == 'nt' else 'clear')
# Chama a função para limpar o terminal
clear_terminal()

#######################################################

nota = 0
contador = 0

while True:
    nota += float(input('Digite uma nota: '))
    contador += 1
    
    clear_terminal()

    print('Nota até o momento: {}'.format(nota))
    print('Total de notas inseridas: {}'.format(contador))
    
    sair = input('\nDeseja digitar mais notas? s/n: ')

    clear_terminal()

    if(sair=='n'):
        break

m = nota / contador

print('Nota total: {}'.format(nota))
print('Total de notas digitadas: {}'.format(contador))
print('A média de notas é {:.2f}'.format(m))