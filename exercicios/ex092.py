from datetime import *
cadastro = {}
anoAtual = date.today().year

while True:
    cadastro['Nome'] = str(input('Nome: '))
    anoNascimento = int(input('Ano de Nascimento: '))
    while anoNascimento < 1923 or anoNascimento > anoAtual:
        anoNascimento = int(input('Digite um ano válido: '))
        break

    cadastro['Idade'] = anoAtual - anoNascimento
    cadastro['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))

    if cadastro['Carteira de Trabalho'] == 0:
        for nome, info in cadastro.items():
            print(f'{nome}: {info}')
        break

    if cadastro['Carteira de Trabalho'] != 0:
        cadastro['Ano de Contratação'] = int(input('Ano de contratação: '))
        while cadastro['Ano de Contratação'] - anoNascimento < 16:
            cadastro['Ano de Contratação'] = int(input('Digite um ano de contratação correto: '))
            break

        cadastro['Salário'] = float(input('Salário: '))
        cadastro['Aposentadoria'] = cadastro['Ano de Contratação'] + 35 - anoNascimento

        for nome, info in cadastro.items():
            print(f'{nome}: {info}')
    break
