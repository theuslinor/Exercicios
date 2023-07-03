def leiaInteiro(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mVocê não digitou um numero inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario não digitou, o valor por padrão será 0\033[m')
            return 0
        else:
            return inteiro


def leiaReal(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mVocê não digitou um numero real!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[mUsuario não digitou, o valor por padrão será 0\033[m')
            return 0
        else:
            return real

inteiro = leiaInteiro('Digite um valor inteiro: ')
real = leiaReal('Digite um valor real: ')
print(f'\033[32mO valor inteiro digitado foi {inteiro} e o real {real}.')