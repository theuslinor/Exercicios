from random import *
nomes, genero, mulheres, idades, veias = [], [], [], [], []
informacoes = {}

with open("nomes.txt", "r") as name:
    listaNomes = [i.strip() for i in name.readlines()]

sexos = ['M', 'F']

while True:

    nome = choice(listaNomes)
    while not nome.isalpha():
        nome = input(('Erro! digite seu nome corretamente: ')).title().strip()
    nomes.append(nome)
    informacoes['nome'] = nomes

    sexo = choice(sexos)
    while sexo not in 'MmFf':
        sexo = str(input('ERRO! Por favor digite apenas M ou F. '))[0]
    genero.append(sexo)
    informacoes['sexo'] = genero

    if sexo in 'fF':
        mulheres.append(nome)


    idade = str(randint(1, 100))
    while not idade.isdigit():
        idade = (input('Erro! digite a idade com números '))
    idades.append(int(idade))
    informacoes['idade'] = idades

    continuar = str(input('Quer continuar? [S/N] '))[0]
    while continuar not in 'SsNn':
        continuar = str(input('Erro! Por favor digite apenas S ou N'))[0]
    if continuar in 'Nn':
        break
media = sum(idades)/len(nomes)

for pos, item in enumerate(idades):
    if item > media:
        veias.append(nomes[pos])
        veias.append(idades[pos])
        veias.append(genero[pos])

print(f'Ao todo temos {len(nomes)} pessoas cadastradas.\n'
      f'A média de idade é de {media:.2f} anos\n'
      f'As mulheres cadastradas foram {", ".join(map(str, mulheres))}.\n'
      f'Lista das pessoas que estão acima da média:')

cont = 0
for i in veias:
    cont+=1
    if cont == 1:
        print(f'Nome = {i}; ', end='')
    elif cont == 2:
        print(f'Idade = {i}; ', end='')
    else:
        print(f'Sexo = {i}; ')
        cont = 0


