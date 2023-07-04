nome = str(input('Qual é o seu nome? ')).lower()
if nome == 'matheus':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'joão':
    print('Seu nome é bem popular')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')
else:
    print('Nome normal')
print('Tenha com bom dia, {}!'.format(nome))