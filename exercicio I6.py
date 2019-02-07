n1 = int(input('Digite um numero: '))
tdev = 0
print('\nDivisores em vermelho\n')
for a in range(1,n1+1):
    if n1%a == 0:
        tdev+=1
        print('\033[31m', end=' ')
    else:
        print('\033[m',end =' ')
    print('{} '.format(a), end=' ')
if tdev==2:
    print('\n\n\033[mO numero {} possue {} divisores e \033[31mÉ PRIMO\033[m'.format(n1, tdev))
else:
    print('\n\n\033[mO numero {} possue {} divisores e \033[31mNÃO É PRIMO\033[m'.format(n1, tdev))