def voto(nascimento):
    from datetime import datetime
    anoAtual = datetime.now().year

    if anoAtual - nascimento <= 15:
        print(f'Com {anoAtual - nascimento} anos de idade não vota.')
    elif anoAtual - nascimento >= 16 and anoAtual - nascimento <= 17 or anoAtual - nascimento > 70:
        print(f'Com {anoAtual - nascimento} anos de idade seu voto é opcional.')
    else:
        print(f'Com {anoAtual - nascimento} anos de idade seu voto é obrigatório.')


voto(int(input('Digite sua data de nascimento: ')))
