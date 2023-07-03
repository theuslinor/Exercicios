pessoas, dado, listaNome, listaPeso,pessoaMaisPesada, pessoaMenosPesada = [], [], [], [], [], []
menorValor = float('inf')
maiorValor = 0
cont = 0
while True:
    cont += 1
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    escolha = str(input('Deseja continuar? [S/N]')).upper()[0]
    if escolha in 'Nn':
        break

print(pessoas)
for pessoa in pessoas:
    if pessoa[1] < menorValor:
        pessoaMenosPesada = pessoa
        menorValor = pessoa[1]
        listaPeso.append(menorValor)
    elif pessoa[1] > maiorValor:
        pessoaMaisPesada = pessoa
        maiorValor = pessoa[1]
        listaPeso.append(maiorValor)


print('Ao todo você cadastrou {} pessoas.'.format(cont))
print('{} é a pessoa mais leve com {}Kg'.format(pessoaMenosPesada[0].title(), menorValor))
print('{} é a pessoa mais pesada com {}Kg'.format(pessoaMaisPesada[0].title(), maiorValor))

