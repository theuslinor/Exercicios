sexo = input('Qual é o seu sexo? [F/M] ').upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    print('Você escreveu um sexo invalido!')
    sexo = input('Qual é o seu sexo? [F/M] ').upper()[0]
if sexo == 'F':
    print('Você é do sexo Feminino!')
else:
    print('Você é do sexo Masculino')
