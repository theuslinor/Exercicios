lista = []
vezes = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    escolha = str(input('Quer continuar? [S/N] ')).upper()[0]
    if escolha == 'N':
        break
lista.sort(reverse=True)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    for posicao, num in enumerate(lista):
        if num == 5:
            vezes.append(posicao + 1)
    print('o numero 5 aparece nas posições {}.'.format(', '.join(map(str, vezes))))
if 5 not in lista:
    print('Não tem o valor 5 nessa lista.')