n1 = str(input('Insira uma frase: '))
n2 = len(n1)
for a in  n1:
    if a in 'aeiou':
        continue
    else:
        print(a,end=' ')