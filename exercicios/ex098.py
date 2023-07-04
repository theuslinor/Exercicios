from time import *
def linha():
    print('-=' * 20)


def contador(inicio, final, passo):
    if inicio < final:
        for y in range(inicio, final+1, passo):
            sleep(0.25)
            print(y, end=' ')
            sleep(0.25)
        print('FIM')
        print(f'Contagem de {inicio} até {final} de {abs(passo)} em {abs(passo)}.')

    else:
        passo = passo * -1
        for y in range(inicio, final-1, passo):
            sleep(0.25)
            print(y, end=' ')
            sleep(0.25)
        print('FIM')
        print(f'Contagem de {inicio} até {final} de {abs(passo)} em {abs(passo)}.')


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
linha()