print('Manipulação de strings')
nome = input('Insira seu nome completo: ')
nomes = nome.split()
n1 = ''.join(nomes)
print('Seu nome é: {}'.format(nome))
print('''Em maiusculo: {} 
Em minusculo: {}
Quantas letras sem os espaços: {}'''.format(nome.upper(), nome.lower(), len(n1)))

print('''Primeiro nome: {}
Tamanho do primeiro nome: {}{}{}'''.format(nomes[0], '\033[4;34m', len(nomes[0]), '\033[4;34m'))