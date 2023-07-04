nome = 'Matheus'
cores = {
        'vermelho': '\033[31m',
        'verde' : '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'lilas': '\033[35m',
        'azulclaro': '\033[36m',
        'cinza' : '\033[37m'}
print('Olá muito prazer em te conhecer, {}{}{}.'.format(cores['azul'], nome, cores['limpa']))