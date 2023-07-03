from random import *
lista = []
for i in range(4):
    players = {}
    numero = randint(1, 6)
    players[f'jogador {i+1}'] = numero
    for jogador, number in players.items():
        print('O {} tirou no {} dado'.format(jogador, number))

ordem = sorted(lista, key=lambda x: x[f'jogador {x}'], reverse=True)

for jogador in ordem:
    for nome, numero in jogador.items():
        print(f'{nome}: {numero}')