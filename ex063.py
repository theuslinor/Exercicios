vezes = int(input('Quantos termos você quer mostrar? '))
primeiro = 0
segundo = 1
print('{} > {} '.format(primeiro, segundo), end='')
cont = 3
while cont <= vezes:
    terceiro = primeiro + segundo
    print('> {} '.format(terceiro),end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print('> THE END')