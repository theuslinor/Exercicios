nome = str(input('Escreva um nome: ').strip().lower())
print('''Quantas vezes aparece a letra "A" {} vezes.
Em que posição ela aparece pela primeira vez? na {}º posição.
Em que posição que ela aparece a ultima vez? na {}º posição.'''.format(nome.count('a'), nome.find('a') + 1, nome.rfind('a') + 1))