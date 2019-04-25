import random as rd
vida_player = 500
sp_player = 100
vida_inimigo = 50
inimigos = []

def criaInimigos():
    for i in range(n):
        inimigos.append([i+1,vida_inimigo])


def ataqueInimigos(vida_player):
    for i in range(len(inimigos)):
        atacado = rd.randint(0, 5)
        if atacado == 0:
            print('O inimigo {} errou o ataque'.format(inimigos[i][0]))
        else:
            print('O inimigo {} tirou {} de vida!'.format(inimigos[i][0], atacado))
            vida_player -= atacado
            if vida_player <= 0:
                print('Você morreu!')
                exit(1)
    return vida_player


def auto_fill(sp_player):
    if sp_player < 100:
        sp_player += 3
    if sp_player > 100:
        sp_player = 100
    return sp_player


n = int(input('Numero de inimigos desejados:'))

criaInimigos()

while len(inimigos)>0:

    print('''Vida:{}
SP:{}'''.format(vida_player, sp_player))
    a = int(input('Deseja atacar (1) ou curar (2): '))

    if a == 1:
        ataque = rd.randint(10,15)
        mob = rd.choice(inimigos)
        nova_vida = mob[1] - ataque

        if nova_vida <= 0:
            print('O inimigo {} morreu!'.format(mob[0]))
            inimigos.remove(mob)

        else:
            mob[1] -= ataque

        print('Você atacou o inimigo {} e tirou {} de vida.'.format(mob[0], ataque))
        vida_player = ataqueInimigos(vida_player)
        sp_player = auto_fill(sp_player)

    if a == 2:

        if sp_player >= 10:
            cura = rd.randint(10,15)
            vida_player += cura

            if vida_player > 500:
                vida_player = 500

            sp_player -= 10
            print('Você curou {} de vida'.format(cura))

        else:
            print('Você não tem Mana para curar.')

        vida_player = ataqueInimigos(vida_player)
        sp_player = auto_fill(sp_player)

print('Você ganhou todos os inimigos foram mortos.')
