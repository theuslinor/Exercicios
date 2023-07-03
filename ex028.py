from random import randrange
escolha = int(input('Escolha um número entre 0 e 5: '))
numero = randrange(6)
if escolha == numero:
    print('Parabéns você acertou o número!')
else:
    print('Você errou, tente novamente')
print('O numero escolhido foi {}'.format(numero))