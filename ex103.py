def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if not gols or gols.isalpha():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campenato.')


ficha(input('Nome: '), (input('Gols: ')))
