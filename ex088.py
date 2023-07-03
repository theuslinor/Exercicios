from random import *
from time import *
import pyfiglet
lista = []
escolha = int(input("Escolha a quantidade de números para a MEGA-SENA: "))

ascii_art = pyfiglet.figlet_format('M E G A - S E N A ')
print('\033[33m', ascii_art, '\033[m')

sleep(0.5)

for i in range(escolha):
    for numeroGerado in range(6):
        while len(lista) < 6:
            sorteio = randint(1, 60)
            lista.append(sorteio)
            lista = list(set(lista))
    print('Jogo {}: {}.'.format(i+1, ', '.join(map(str, sorted(lista)))))
    lista.clear()
    sleep(0.5)
