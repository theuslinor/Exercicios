def leiaInt(numero):
    while not numero.isdigit():
        print('\033[31mErro, digite um número!\033[m')
        numero = leiaInt(input('Digite um número: '))
    return int(numero)

numero = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {numero}.')