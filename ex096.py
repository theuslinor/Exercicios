def area():
    lar = float(input('LARGURA (M): '))
    com = float(input('COMPRIMENTO (M): '))
    print(f'A área de um terreno {lar}x{com} é de \033[32m{lar*com}m²\033[m.')


area()


'''def area(larg, comp):
    a = larg*comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m².')
    

l = float(input('Largura'))
c = float(input('Comprimento'))
area(l, c)'''
