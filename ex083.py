'''cont = cont1 = 0
expre = str(input('Digite uma Expressão: '))
for parenteses in expre:
    if '(' in parenteses:
        cont=cont+1
    if ')' in parenteses:
        cont1=cont1 + 1
if cont == cont1:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
    '''

# Jeito do professor

expr = str(input('Digite sua expressão: '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')