from time import sleep
listatimes = []
with open('times.txt', 'r', encoding='UTF-8') as arquivo:
    for time in arquivo:
        listatimes.append(time.strip().title())
sleep(0.25)
print('Lista de times do Brasileirão: \033[32:1m{}\033[m.'.format(', '.join(listatimes)))
sleep(0.25)
print('Os 5 primeiros times são \033[32:1m{}\033[m.'.format(', '.join(listatimes)))
sleep(0.25)
print('Os 4 ultimos times são \033[32:1m{}\033[m.'.format(', '.join(listatimes[-4:])))
sleep(0.25)
print('Times em ordem alfabética: \033[32:1m{}\033[m.'.format(', '.join(sorted(listatimes))))
sleep(0.5)
escolha = str(input('Escolha um time: ')).title()
posicao = listatimes.index(escolha) + 1
if posicao >= 1 and posicao < 7:
    print('O \033[34m{}\033[m está em \033[34m{}°\033[m colocação.'.format(escolha, posicao))
elif posicao >= 7 and posicao < 8:
    print('O \033[33m{}\033[m está em \033[33m{}°\033[m colocação.'.format(escolha, posicao))
elif posicao >= 9 and posicao < 14:
    print('O \033[32m{}\033[m está em \033[32m{}°\033[m colocação.'.format(escolha, posicao))
elif posicao >= 15 and posicao < 16:
    print('O {} está em {}° colocação.'.format(escolha, posicao))

else:
    print('O \033[31m{}\033[m está em \033[31m{}°\033[m colocação.'.format(escolha, posicao))