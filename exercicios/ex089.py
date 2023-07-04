lista, subLista = [], []
cont = 0
while True:
    subLista.append(str(input('Nome: ')).title())
    subLista.append(float(input('Nota 1: ')))
    subLista.append(float(input('Nota 2: ')))
    lista.append(subLista[:])
    subLista.clear()

    continuar = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if continuar == 'N':
        break


print('{:2s} {:25s} {:5s}'.format('No.', 'Nome', 'Média'))
for pos, alunos in enumerate(lista):
    media = (alunos[1] + alunos[2]) / 2
    print('{:2d} {:25s} {:5.2f}'.format(pos+1, alunos[0], media))
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe) '))-1

    if 0 <= escolha <= len(lista):
        print('A nota de {} são {} e {}.'.format(lista[escolha][0], lista[escolha][1], lista[escolha][2]))
    elif escolha == 998:
        print('Finalizando')
        break
