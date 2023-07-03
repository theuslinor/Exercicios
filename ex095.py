from random import *
historicoJogador = {}
jogos, listaMajor, nomes_escolhidos = [], [], []

with open("jogadores.txt", "r", encoding='UTF-8') as jogadores:
    listaNomes = [i.strip() for i in jogadores.readlines()]



while True:
    historicoJogador = {}
    jogos.clear()

    while True:
        nome = choice(listaNomes)
        if nome not in nomes_escolhidos:
            nomes_escolhidos.append(nome)
            break
    historicoJogador['jogador'] = nome

    numeroPartidas = randint(1, 5)

    for i in range(0, numeroPartidas):
        jogos.append(randint(0, 6))
        '''jogos.append(int(input(f'Quantos gols {historicoJogador["jogador"]} fez na {i+1}º partida: ')))'''
    historicoJogador['gols'] = jogos[:]
    historicoJogador['total'] = sum(jogos)
    historicoJogador.copy()
    listaMajor.append(historicoJogador)

    try:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar == 'N':
            break
    except Exception as erros:
        print('Digite algo! ')

print('Cont'.center(5), 'Nome'.center(20), 'Gols'.center(20), 'Total de Gols'.center(20))

# Organizador de artilharia
listaMajor = sorted(listaMajor, key=lambda x: x['total'], reverse=True)

for pos, dadosJogador in enumerate(listaMajor):
    print(str(pos+1).center(5), end=' ')
    for k, v in dadosJogador.items():
        if k == 'gols':
            print(f"{', '.join(map(str, v)).center(22)}", end='')
        else:
            print(f'{str(v).center(20)}', end='')
    print()

while True:

    try:
        escolherJogador = int(input('\nMostrar dados de qual jogador? (999 para parar) '))-1
        if escolherJogador >= 998:
            break
        print(f"\nLevantamento do jogador: {listaMajor[escolherJogador]['jogador']}:")

        for pos, gols in enumerate(listaMajor[escolherJogador]['gols']):
            print(f'No jogo {pos+1} fez {gols} gols.')

    except Exception as erro:
        print(erro)
        print('O numero informado é maior que o numero de jogadores na lista.')

print('\n \033[35mFim do programa')
