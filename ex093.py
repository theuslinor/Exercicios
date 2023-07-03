historicoJogador = {}
jogos = []

historicoJogador['jogador'] = str(input('Nome do Jogador: ')).title().strip()
numeroPartidas = int(input(f"Quantas partidas {historicoJogador['jogador']} jogou? "))

for i in range(0, numeroPartidas):
    jogos.append(int(input(f'Quantos gols {historicoJogador["jogador"]} fez na {i+1}º partida: ')))
historicoJogador['gols'] = jogos
historicoJogador['total'] = sum(jogos)
print('=-' * 30)
print(historicoJogador)
print('=-' * 30)

for n, a in historicoJogador.items():
    print('O campo {} tem o valor {}.'.format(n, a))
print('=-' * 30)

for pos, gols in enumerate(historicoJogador['gols']):
    print('Na {}º partida, {} fez {} gols.'.format(pos+1, historicoJogador['jogador'], gols))
print('Foi um total de {} gols'.format(historicoJogador['total']))
print('=-' * 30)