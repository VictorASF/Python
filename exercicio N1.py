def media(n1=0,n2=0):
    m = (n1+n2)/2
    return m

def nome():
    print('Victor Augusto de Souza Fonseca')
def nomecompleto(nome1='',nome2=''):
    print('Nome completo: {}'.format(nome1+' '+nome2))
#def inverso(pal = ''):
#    for i in range (len(pal)-1,-1,-1):
#        print(pal[i],end='')

def inverso(palavra = ''):
   inverter = list(palavra)
   inverter.reverse()
   invertido =''.join(inverter)
   print('{} --> {}'.format(palavra,invertido))

m1 = float(input('Insira a primeira nota: '))
m2 = float(input('Insira a segunda nota: '))
r = media(m1,m2)
print('A media entre {:.2f} e {:.2f} é {:.2f}'.format(m1, m2, r))
nome()
no1 = str(input('Insira o primeiro nome: '))
no1 = no1.capitalize()
no2 = str(input('Insira o sobrenome: '))
no2 = no2.capitalize()
nomecompleto(no1,no2)
pala = str(input('Insira uma palavra: '))
inverso(pala)


