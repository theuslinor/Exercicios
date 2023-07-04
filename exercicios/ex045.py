from random import randint
from time import sleep
jokenpo = ('\033[1:34mPedra\033[m', '\033[1:35mPapel\033[m', '\033[1:36mTesoura\033[m')
computador = randint(0, 2)
escolha = int(input('Jokenpo'
                    '\n[ 0 ] \033[1:34mPedra\033[m'
                    '\n[ 1 ] \033[1:35mPapel\033[m'
                    '\n[ 2 ] \033[1:36mTesoura\033[m'
                    '\nEscolha: '))
if escolha >= 3:
    print(' \033[1:31mDigite um numero válido\033[m')
    exit()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.25)
if computador == 0:
    if escolha == 0:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[0], jokenpo[0]))
        print('\033[1:33mDeu empate!\033[m')
    elif escolha == 1:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[1], jokenpo[0]))
        print('\033[1:32mJogador\033[m \033[1:32mvenceu!\033[m')
    elif escolha == 2:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[2], jokenpo[0]))
        print('\033[1:31mComputador\033[m \033[1:31mvenceu!\033[m')
if computador == 1:
    if escolha == 0:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[0], jokenpo[1]))
        print('\033[1:31mComputador\033[m \033[1:31mvenceu!\033[m')
    elif escolha == 1:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[1], jokenpo[1]))
        print('\033[1:33mDeu empate!\033[m')
    elif escolha == 2:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[2], jokenpo[1]))
        print('\033[1:32mJogador\033[m \033[1:32mvenceu!\033[m')
if computador == 2:
    if escolha == 0:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[0], jokenpo[2]))
        print('\033[1:32mJogador\033[m \033[1:32mvenceu!\033[m')
    elif escolha == 1:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[1], jokenpo[2]))
        print('\033[1:31mComputador\033[m \033[1:31mvenceu!\033[m')
    elif escolha == 2:
        print('\033[1:32mJogador\033[m escolheu {}'
              '\n\033[1:31mComputador\033[m escolheu {}'.format(jokenpo[2], jokenpo[0]))
        print('\033[1:33mDeu empate!\033[m')