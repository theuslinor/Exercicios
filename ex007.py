n1 = float(input('O aluno tirou qual nota em Matematica? '))
n2 = float(input('O aluno tirou qual nota em Portugues? '))
media = (n1 + n2) / 2
print('O aluno tirou \033[31m{:.1f}\033[m em Matematica e \033[33m{:.1f}\033[m em Portugues, e a média dele foi \033[32m{:.1f}\033[m.' .format(n1, n2, media))