while True:
    n1 = str(input('Insira o sexo [M/F]: '))
    n1 = n1.upper()
    if n1 in 'M':
        print('O sexo escolhido foi \033[4mMasculino\033[m')
        break
    elif n1 in 'F':
        print('O sexo escolhido foi \033[4mFeminino\033[m')
        break
    print('\033[31mValor incorreto\033[m', end=' ')
