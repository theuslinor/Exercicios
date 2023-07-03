from random import randint
comp = randint(0, 10)
tentativa = 1
player = int(input('Digite um numero de \033[32m0 a 10\033[m: '))
while player != comp:
    tentativa = tentativa + 1
    if player < comp:
        player = int(input('\033[33mQuase\033[m, um pouco acima, digite um numero de {} até 10: '.format(player)))
    else:
        player = int(input('\033[31mQuase\033[m, um pouco abaixo, digite um numero de {} até 0: '.format(player)))
if tentativa == 1:
    print('\033[32mParabens!!\033[m você acertou de \033[32mprimeira\033[m, o número sorteado foi \033[32m{}\033[m.'.format(comp))
elif tentativa >= 4:
    print('Depois de \033[31m{}\033[m tentativas você acertou, o número sorteado foi \033[32m{}\033[m.'.format(tentativa, comp))
else:
    print('Depois de \033[32m{}\033[m tentativas você acertou, o número sorteado foi \033[32m{}\033[m.'.format(tentativa, comp))