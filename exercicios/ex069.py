from time import sleep
homem = mulher20 = maior = idade = cont = 0
sexo = continuar =  ''
while True:
    sexo = continuar =  ''
    idade = 0
    cont+=1
    print('-' * 19)
    print(f'Cadastre {cont}ª Pessoa ')
    print('-' * 19)
    sleep(0.5)
    while idade >= 100 or idade <= 0:
        idade = int(input('Digite uma idade: '))
    sleep(0.5)
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [\033[33mM\033[m/\033[35mF\033[m] ')).upper()[0]
    sleep(0.5)
    if sexo == 'F' and idade < 20:
            mulher20+= 1
    if sexo == 'M':
        homem+= 1
    if idade >= 18:
        maior+= 1
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        sleep(0.5)
        if continuar != 'N' and continuar != 'S':
            print('Escreva corretamente!')
        else:
            break
    if continuar == 'N':
        break
sleep(0.5)
print('Foram cadastradas o total de \033[32m{}\033[m pessoas'.format(cont))
sleep(0.25)
print('Total de pessoas com mais de 18 anos: \033[36m{}\033[m'.format(maior))
sleep(0.25)
print('Ao todo temos \033[33m{}\033[m homens cadastrados.'.format(homem))
sleep(0.25)
print('E temos \033[35m{}\033[m mulheres com menos de 20 anos.'.format(mulher20))