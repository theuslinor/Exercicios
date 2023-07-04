velocidade = int(input('Digite a velocidade: '))
if velocidade <= 75:
    print('Você está na velocidade, DIRIJA COM CUIDADO!')
elif velocidade <= 79:
    print('Você está proximo da velocidade máxima, DIMINUA A VELOCIDADE!')
else:
    velocidade2 = velocidade - 80
    multa = velocidade2 * 7.00
    print('VOCÊ ESTÁ {}KM ACIMA DA VELOCIDADE'.format((velocidade2)))
    print('VOCÊ FOI MULTADO EM R${:.2f}'.format(multa))