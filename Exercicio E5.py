f1 = input('Entre com uma frase para ser analisada: ')
f1 = f1.lower()
f2 = f1.replace(' ','')
f1 = f1.strip()

print('''Quantas vezes aparece o "A": {}
A posiçao que aparece pela primeira vez (0-{}): {}
A posição que aparece pela ultima vez (0-{}): {} '''.format(f1.count('a'), len(f1)-1, f1.find('a'), len(f1)-1, f1.rfind('a')))