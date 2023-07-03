idades = []
maior = age = idade = 0
sexo = nome = maisvelho = ''
for c in range(0, 2):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    lista = [nome, idade, sexo]
    idades.append(lista)
    while sexo != 'M' and sexo != 'F':
        print('Sexo invalido!')
        sexo = input('Digite novamente o sexo: ')
    if sexo == 'M' and idade > maior:
        maior = idade
        maisvelho = nome
    if sexo == 'F' and idade < 20:
        age =+ 1
if sexo == 'F' and idade < 20:
    print('Existem {} mulheres com menos de 20 anos'.format(age+1))
media_idade = sum(idade for nome, idade, sexo in idades) / len(idades)
if sexo == 'F' and idade > 20:
    print('Não tem mulheres abaixo de 20 anos')
elif sexo == 'M' and idade > maior:
    maior = idade
    maisvelho = nome
    print('O nome do homem mais velho é {}'.format(maisvelho))
print('A média de idade do grupo é de {} anos de idade'.format(media_idade))
