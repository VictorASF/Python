c1 = input('Digite o nome de uma cidade: ')
c1 = c1.title()
c2 = c1.split()
if c2[0] =='Sao' or c2[0] == 'São':
    print('''A cidade é: {}
E ela começa com "São"'''.format(c1))
else:
    print('''A cidade é: {}
E ela nao começa com "São" '''.format(c1))
