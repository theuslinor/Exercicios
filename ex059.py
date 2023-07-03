from time import sleep
var = True
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while var == True:
    escolha = int(input('[ 1 ] Somar\n'
                        '[ 2 ] Multiplicar\n'
                        '[ 3 ] Maior\n'
                        '[ 4 ] Novos Números\n'
                        '[ 5 ] Sair do Programa\n'
                        'Qual a sua escolha: '))
    if escolha == 1:
        soma = num1 + num2
        print('Processando...')
        sleep(5)
        print('A soma de {} mais {} é igual a {}.'.format(num1, num2, soma))
    elif escolha == 2:
        multi = num1 * num2
        print('Processando...')
        sleep(0.5)
        print('A multiplicação de {} vezes {} é igual a {}.'.format(num1, num2, multi))
    elif escolha == 3:
        if num1 > num2:
            print('Processando...')
            sleep(0.5)
            print('O número {} é maior que o número {}.'.format(num1, num2))
        elif num2 > num1:
            print('Processando...')
            sleep(0.5)
            print('O número {} é maior que o número {}.'.format(num2, num1))
        else:
            print('Processando...')
            sleep(0.5)
            print('O número {} é igual ao número {}.'.format(num1, num2))
    elif escolha == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Processando...')
        sleep(0.5)
        print('Finalizando o programa...')
        exit()
    else:
        print('O número digitado está incorreto, o programa vai reiniciar em')
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        var = True
    sleep(0.5)
    if escolha == 4:
        var = True
    elif escolha > 5:
        var = True
    else:
        again = int(input('Gostaria de ir de novo?\n'
                          '[ 1 ] Sim\n'
                          '[ 0 ] Não\n'
                          'Escolha: '))
        if again == 1:
            var = True
        elif escolha > 5:
            var = True
        else:
            sleep(0.5)
            print('Finalizando o programa...')
            var = False
