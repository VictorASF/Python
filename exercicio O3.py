arq = open ('convidados.txt', 'a')

for a in range(0):
    d = int(input('Insira o codigo: '))
    nome = str(input('Insira o nome: ').strip().capitalize())
    cidade = str(input('Insira a Cidade: ').strip().capitalize())
    estado = str(input('Insira o estado[Ex: RJ,SP,RS]: ').strip().upper())
    arq.writelines('{:<8} {:<40} {:<30} {:<2}\n'.format(d, nome, cidade, estado))
arq.close()

arq = open('convidados.txt', 'r')
arq.seek(0)
linha = arq.readline()
while len(linha)>0:
    print('O convidado \033[1m{}\033[m cujo nome é \033[31m{}\033[m mora em \033[4m{}/{}\033[m'.format(linha[0:8].strip(),
                                                                                                       linha[8:48].strip(),
                                                                                                       linha[48:81].strip(),
                                                                                                       linha[81:83].strip()))
    linha = arq.readline()