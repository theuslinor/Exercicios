lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Você digitou um valor repetido, não irei adicionar.')
    else:
        lista.append(numero)
    escolha = str(input('Quer continuar? [S/N] ')).upper()[0]
    if escolha in 'N':
        break
print('A ordem da lista é {} '.format(sorted(lista)))