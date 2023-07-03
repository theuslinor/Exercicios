alunos = {}
escola = []
for i in range(2):
    alunos['nome'] = str(input('Nome: ')).title()
    alunos['media'] = float(input('Media: '))
    escola.append(alunos.copy())
for inf in escola:
    for nome, media in inf.items():
        if inf['media'] < 3.9:
            situacao = 'Reprovado'
        elif inf['media'] < 6.9:
            situacao = 'Recuperação'
        elif inf['media'] <= 10:
            situacao = 'Aprovado'
        print(f'{nome} igual a {media}', end=' ')
    print(situacao)
