d1 = {}
d2 = {}
d3 = {}
a = str(input('Inserir nome: '))
a = a.capitalize()
d1['nome'] = a
h = str(input('Sobrenome: '))
h = h.capitalize()
d1['sobrenome'] = h
b = int(input('Inserir a idade: '))
d1['idade'] = b
c = float(input('Inserir peso: '))
d1['peso'] = c

print('{} {} com {} anos e pesando {} Kg'.format(d1['nome'],
                                                 d1['sobrenome'],
                                                 d1['idade'],
                                                 d1['peso']))