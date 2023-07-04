import datetime
sexo = str(input('Você é do sexo Feminino ou Masculino: [F] ou [M] ')).upper()
if sexo == 'F':
    print('O serviço de alistamento militar é somente para homens.')
else:
    ano_nasc = int(input('Digite o ano de nascimento: '))
    idade = datetime.datetime.today().year - ano_nasc
    if idade > 18:
        alist = idade - 18
        print('Você já deveria ter se alistado há \033[31m{} anos.\033[m'.format(idade - 18))
        print('Seu alistamento foi em \033[31m{}.\033[m'.format(ano_nasc + 19))
    elif idade < 18:
        print('Você deverá se alistar daqui {} anos.\033[m'.format(18 - idade))
        print('Você irá se alistar em {}.'.format(ano_nasc + 18))
    else:
        print('\033[34mVocê está no ano de alistamento, procure o quartel mais próximo!\033[m')
