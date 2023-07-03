import random
'''n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''
lista = []
for aluno in range(1, 5):
    lista.append(str(input(f'Digite o nome do {aluno}º aluno: ')))
random.shuffle(lista)
print('O aluno escolhido foi o {}.'.format(lista))