arq = open('cores.txt', 'r')
print('Mostrando o arquivo no FOR')
print('-'*30)
for linha in arq:
    print(linha)
print('-'*30)
arq.seek(0)
linhas = arq.readline()
print('Mostrando o arquivo no WHILE')
print('-'*30)
while len(linhas) > 0:
    print(linhas)
    linhas = arq.readline()
print('-'*30)
arq.close()