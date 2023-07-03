metros = float(input('Digite um numero de metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
jar = metros * 0.9144
pe = metros * 1.094
print('{} metros em km é \033[31m{}km\033[m, em hm é igual a \033[32m{}hm\033[m, em dam é igual a \033[33m{}dam\033[m, em dm é igual a \033[34m{}dm\033[m, em cm é igual \033[35m{}cm\033[m, em mm é igual \033[36m{}mm\033[m, em jardas é igual a \033[37m{}\033[mjardas, em pés é igual a \033[7;30;40m{}pés\033[m' .format(metros, km, hm, dam, dm, cm, mm, jar, pe))

