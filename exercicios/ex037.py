num = int(input('Digite um numero qualquer: '))
choice = int(input('Escolha como você quer converter seu numero: \n [ 1 ] Binário \n [ 2 ] Octal \n [ 3 ] Hexadecimal \n Digite um número: '))
if choice == 1:
    numero_binario = bin(num)[2:]
    print('{} é {} em Binário.'.format(num, numero_binario))
elif choice == 2:
    numero_octal = oct(num)[2:]
    print('{} é {} em Octal.'.format(num, numero_octal))
elif choice == 3:
    numero_hexa = hex(num)[2:]
    print('{} é {} em Hexadecimal.'.format(num, numero_hexa))
else:
    print('Escolha um número válido')