d1 = {1: ('HB20 1.0 Comfort Plus', 33590),
      2: ('2008 Allure 1.6 16V', 71990),
      3: ('Argo Drive 1.0 Firefly', 44990),
      4: ('Corola Sedan SEG 1.8 16V', 44900),
      5: ('KA 1.0 SE', 34900),
      6: ('Fox 1.0 VHT', 26990)}
def carros():
    print('Cod.    Carro')
    print('-'*30)
    for a in d1:
        print(' {}      {}'.format(a, d1[a][0]))
    print(' 0      Sair do programa')
while True:
    carros()
    opcao = int(input('\nCodigo:'))
    if 0< opcao <7:
        print('Valor do carro {} eh de R$:{:.2f}'.format(d1[opcao][0],d1[opcao][1]))
        input('Pressione <ENTER> para continuar')
    elif opcao == 0:
        print('Saindo do programa')
        break
    else:
        print('Opcao invalida ')