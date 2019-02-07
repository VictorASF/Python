soma = 0
for a in range (1,500,2):
    if a%3==0:
        print(a)
        soma = soma + a
    else:
        continue
print('Soma :{}'.format(soma))