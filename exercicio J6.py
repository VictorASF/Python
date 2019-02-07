idade = 0
mulher = 0
homem = 0
while True:
    n1 = int(input('Idade: '))
    n2 = str(input('Sexo (M/F): '))
    n2 = n2.upper()
    if 18 <= n1 < 21:
        idade += 1
        if n2 == 'M':
            homem += 1
    elif n1 >= 21:
        idade += 1
        if n2 == 'F':
            mulher += 1
        elif n2 == 'M':
            homem += 1
    n3 = str(input('Deseja continuar (S/N)?: '))
    n3 = n3.upper()
    if n3 == 'N':
        break
print(
    'Pessoas com + de 18 anos: {}\nHomens cadastrados: {}\nMulheres com + de 21 anos: {}'.format(idade, homem, mulher))
