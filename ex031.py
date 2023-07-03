viagem = float(input('Qual a distancia de sua viagem? '))
if viagem >= 200:
    longa = viagem * 0.45
    print('Você irá pagar R${:.2f} pela viagem'.format(longa))
else:
    curto = viagem * 0.50
    print('Você irá pagar R${:.2f} pela viagem'.format(curto))