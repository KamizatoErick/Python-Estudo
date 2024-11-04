# Faça um programa que mostre na tela uma contagem regressiva
# para estouros de fogos de articícios, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.

import time
import emoji #documentação https://pypi.org/project/emoji/

for c in range(1,11):
    print(c)
    time.sleep(1)

print(emoji.emojize(":fireworks::sparkler:"))
