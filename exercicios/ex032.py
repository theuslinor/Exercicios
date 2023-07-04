from calendar import isleap
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
  ano = date.today().year
if isleap(ano):
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('Ano {} não é um ano BISSEXTO'.format(ano))





''''from datetime import date
ano = int(input('Que ano quer analisar?? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano - date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {}NÃO é BISSEXTO'.format(ano))'''
