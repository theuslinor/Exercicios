n1 = str(input('Nota em Matemática e Português: ')).split()
if len(n1) >= 3:
    print('você digitou um numero a mais, faça novamente.')
else:
    n1 = float(n1[0]), float(n1[1])
    if n1[0] > 10 or n1[1] > 10:
        print('\033[31mTem algo de errado em sua nota, em uma da notas você tirou mais que 10!\033[m')
    else:
        media = (n1[0] + n1[1]) / 2
        if media <= 5.0:
            print('Sua média foi {:.2f}, você foi \033[31mREPROVADO!\033[m'.format(media))
        elif media <= 6.9:
            print('Sua média foi {:.2f}, você está de \033[33mRECUPERAÇÃO\033[m'.format(media))
        else:
            print('Sua média foi {:.2f}, você está  \033[32mAPROVADO!\033[m'.format(media))