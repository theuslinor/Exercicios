import modulos.aula.cadastro as mod
from time import sleep
from random import choice, randint
with open("nomes.txt", "r") as name:
    listaNomes = [i.strip() for i in name.readlines()]

while True:
    try:
        mod.menu(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do sistema'])
        opcao = int(input('\033[32mSua opção: \033[m'))
        sleep(0.5)
        if opcao == 1:
            mod.cadastrarUsuario(choice(listaNomes), str(randint(10,99)))

        elif opcao == 2:
            mod.lerUsuario()

        elif opcao == 3:
            mod.cabecalho('\033[35mFim do programa.\033[m')
            break
        else:
            mod.cabecalho('\033[31mVocê digitou um numero invalido!\033[m')
            sleep(0.5)
            continue
    except (ValueError):
        mod.cabecalho('\033[31mVocê digitou uma letra ao invés de um número.\033[m')
        sleep(0.5)
        continue
