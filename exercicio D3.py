'''
Exercicio 3D Curso de python udemy


Victor A. de Souza Fonseca
'''

from random import choice
#Primeiro pega o nome dos alunos
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluo: ")
#É criado uma lista para usar o random.choice
list = [a1,a2,a3]
print("Escolhido: {}".format(choice(list)))