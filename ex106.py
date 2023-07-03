def ajuda():
    """
    Responde sua duvida
    :return: Sua duvida
    """
    from time import sleep

    cor = 32
    while True:
        print('\033[43m-='*20)
        print('SISTEMA DE AJUDA PyHelp'.center(40))
        print('-='*20)

        duvida = str(input('\033[mFunção ou Biblioteca > '))

        if duvida == 'sair':
            break
        sleep(0.5)
        print('\033[40:32m-=' * 20)
        print(f"Acessando o manual do comando '{duvida}'".center(40))
        print('-=' * 20)

        sleep(0.5)
        print(f'\033[{cor}m')
        help(duvida)
        print('\033[m')


        cor+=1
        if cor == 37:
            cor = 32
    print('The End')


ajuda()

