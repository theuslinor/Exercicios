from random import randint
cont = 0
while True:
    computador = randint(0, 10)
    while True:
        numero = int(input('Digite um numero[0/10]: '))
        if 0 <= numero <= 10:
            break
        print('Digite um número entre 0 e 10.')
    imp_par = str(input('Impar ou Par? [P/I]')).strip().upper()[0]
    soma = computador + numero
    print(f'Você jogou {numero} e o computador jogou {computador} e a soma dos dois é {numero + computador}.')
    if imp_par == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if imp_par == 'I':
        if soma % 2 != 0 and soma % 3 == 0:
            print('Você venceu!')
            cont += 1
            print(soma)
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')