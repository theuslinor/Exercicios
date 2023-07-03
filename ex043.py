altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = (peso / (altura**2)) * 10000
if imc < 18.5:
    print('Seu IMC é \033[4:36m{:.2f}\033[m, \033[4:36mVocê está ABAIXO DO PESO.\033[m'.format(imc))
elif imc < 25:
    print('Seu IMC é \033[4:32m{:.2f}\033[m, \033[4:32mVocê está no PESO IDEAL.\033[m'.format(imc))
elif imc < 30:
    print('Seu IMC é \033[4:33m{:.2f}\033[m, \033[4:33mVocê está com SOBREPESO.\033[m'.format(imc))
elif imc < 40:
    print('Seu IMC é \033[4:35m{:.2f}\033[m, \033[4:35mVocê está com OBESIDADE.\033[m'.format(imc))
else:
    print('Seu IMC é \033[4:31m{:.2f}\033[m, \033[4:31mVocê está com OBSIDADE MÓRBIDA.\033[m'.format(imc))