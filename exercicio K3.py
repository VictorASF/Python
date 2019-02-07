pessoas = [[], []]
idade = 0
while True:
    nome = str(input('Insira um nome: '))
    idade = str(input('Insira uma idade: '))
    nome = nome.strip()
    nome = nome.capitalize()
    if nome != '' and idade.isnumeric():
        pessoas[0].append(nome)
        pessoas[1].append(idade)
    else:
        break
for idx in range(len(pessoas[0])):
    print('Indice {}. {} {} anos'.format(idx, pessoas[0][idx], pessoas[1][idx]))
if len(pessoas[0])>0:
    print('Primeira Pessoa: {} {} anos'.format(pessoas[0][0], pessoas[1][0]))
    print('Ultima pessoa: {} {} anos'.format(pessoas[0][-1], pessoas[1][-1]))