dia = int(input('Quantos dias você rodou com o carro? '))
km = float(input('Quantos km você rodou com o carro? '))
pkm = km * 0.15
pdia = dia * 60.00
print('você percorreu o total de {:.2f}km, e ficou com o carro {:.2f} dias, total a se pagar é R${:.2f}'.format(km, dia , pdia + pkm))