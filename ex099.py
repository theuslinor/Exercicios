from time import *

def linha():
    print('=-' * 30)


print('Analisando os valores passados...')
linha()
def maior(* num):

    cont = 31
    for i in num:
        sleep(0.5)
        print(f'\033[{cont}m{i}\033[m', end=' ')
        cont+=1
        if cont == 38:
            cont = 31

    sleep(0.5)
    print(f'Foram informados \033[32m{len(num)}\033[m valores ao todo.')
    sleep(0.5)
    linha()
    print(f'O maior valor informado foi de \033[32m{max(num)}\033[m.')
    linha()

maior(5, 76, 98, 34, 23, 54, 76, 34, 6, 234, 546)
