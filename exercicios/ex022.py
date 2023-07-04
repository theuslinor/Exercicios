nome = 'Matheus de Barros dos Santos'
mais = nome.upper()
menor = nome.lower()
esp = nome.replace(' ', '')
nome = nome.split()
ind = len(nome[2])
print("""
Seu nome completo em maiúsculo: {}
Seu nome em minúsculo: {}
{} é a quantidade de letras no seu nome completo.
Seu nome tem o total de {} letras.""".format(mais, menor, len(esp), ind))

'''nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa =nome.split()
print('Seu primeiro nome é {} e  ele tem {} letras'.format(separa[0], len(separa[0])))'''