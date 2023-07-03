from datetime import date
nasc = int(input('Digite seu ano de nascimento:  '))
if len(str(nasc)) != 4:
    print('\033[4:31mVocê digitou um ano incorreto!\033[m')
else:
    idade = date.today().year - nasc
    if idade <= 9:
        print('O atleta tem \033[4:36m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:36mMIRIM\033[m')
    elif idade <= 14:
        print('O atleta tem \033[4:35m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:35mINFANTIL\033[m')
    elif idade <= 19:
        print('O atleta tem \033[4:33m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:33mJUNIOR\033[m')
    elif idade <= 25:
        print('O atleta tem \033[4:32m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:32mSÊNIOR\033[m')
    elif idade <= 100:
        print('O atleta tem \033[4:34m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:34mMASTER\033[m')
    else:
        print('O atleta tem \033[4:31m{} anos.\033[m'.format(idade))
        print('Classificação: \033[4:31mENTERRA QUE TA MORTO\033[m')