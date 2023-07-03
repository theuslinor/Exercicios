from datetime import date
maior = menor = 0
anoAtual = date.today().year
for c in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    while nascimento > anoAtual or nascimento < 1900:
        if nascimento > anoAtual:
            nascimento = int(input('O ano não pode ser maior que {}, digite uma data correta: '.format(anoAtual)))
        elif nascimento < 1900:
            nascimento = int(input('O ano não pode ser menor que 1900, digite uma data correta: '))
    idade = anoAtual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tem {} pessoas maiores de idade'.format(maior))
print('Tem {} pessoas menores de idade'.format(menor))
