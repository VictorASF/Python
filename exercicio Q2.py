import os

os.chdir('C:/Users/MARIO/Desktop/Script Python')
os.mkdir('NOME')
print(os.listdir('.'))
os.renames('NOME','BACKUP')
print(os.listdir('.'))