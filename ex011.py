altura = float(input('Qual é a altura da perede? '))
largura = float(input('Qual é a largagura da parede? '))
quadrado = altura * largura
tinta = quadrado / 2
print('\033[7:30mUma parede com altura de {:.2f} metros e {:.2f} metros de largura, totalizando {:.2f}² vai precisar de {:.2f} litros de tinta para ser pintada\033[m' .format(altura, largura, quadrado, tinta))