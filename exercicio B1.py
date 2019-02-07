print("="*8+"Soma"+"="*8)
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
print("A soma de {} com {} é igual a {}{}{}".format(n1, n2, '\033[4;35m', n1+n2, '\033[1;35m'))