n1 = str(input('Digite uma frase: '))
n2 = len(n1)
#o "-1" junto ao n2 é porque a cadeia de string funciona igual o c++ começando do zero nao do um
for a in range (n2-1, -1, -1):
    print(n1[a],end=' ')