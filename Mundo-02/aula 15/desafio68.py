# Faça um programa que jogue par ou impar
# com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vítorias
# consecutivas que ele conquistou no final do jogo.
import random
print('\n')
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')

vUsuario = 0
while True:
    print('=-'*20)
    computador = random.randint(0,10)
    usuario = int(input('Diga um valor: '))
    escolha = ' '
    
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar?[P/I] ')).upper().strip()[0]
    
    print(f'Você jogou {usuario} e o computador {computador}. Total de {usuario+computador}', end='')
    print(' DEU PAR' if (usuario+computador) % 2 == 0 else 'DEU ÍMPAR')
    print('-'*20)
    
    if escolha == 'P' and (usuario+computador) % 2 == 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        vUsuario += 1
    elif escolha == 'I' and (usuario+computador) % 2 == 1:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        vUsuario += 1
    else:
        break
print('GAME OVER!')
print(f'Você venceu {vUsuario} vezes.')