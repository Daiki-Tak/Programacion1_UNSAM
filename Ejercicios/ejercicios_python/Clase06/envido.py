# envido.py
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]


def generar_mano():
    return random.sample(naipes, 3)

def calcular_envido(mano):
    t=mano
    envido=0
    if t[0][1] == t[1][1]:
        if t[0][0] > 7:
            envido = 20 + int(t[1][0])
        elif t[1][0] > 7:
            envido = 20 + int(t[0][0])
        else:
            envido = 20 + int(t[0][0]) + int(t[1][0])
    if t[0][1] == t[2][1]:
        if t[0][0] > 7:
            envido = 20 + int(t[2][0])
        elif t[2][0] > 7:
            envido = 20 + int(t[0][0])
        else:
            envido = 20 + int(t[0][0]) + int(t[2][0])
    if t[1][1] == t[2][1]:
        if t[1][0] > 7:
            envido = 20 + int(t[2][0])
        elif t[2][0] > 7:
            envido = 20 + int(t[1][0])
        else:
            envido = 20 + int(t[1][0]) + int(t[2][0])
    return envido

N = 100000
E= [0,0,0]

for i in range(N):
    envido=calcular_envido(generar_mano())
    if envido > 30:
        E[envido - 31] += 1
prob_Ehi = sum(E) / N
prob_E31 = E[0] / N
prob_E32 = E[1] / N
prob_E33 = E[2] / N

print(f'Jugué {N} manos, de las cuales {sum(E)} fueron un envido alto. De esas manos, en {E[0]} saqué 31, en {E[1]} saqué 32 y en {E[2]} saqué 33.')
print(f'Podemos estimar la probabilidad de sacar un envido alto como {prob_Ehi:.5f}, y la de sacar 31 como {prob_E31:.5f}, la de sacar 32 como {prob_E32:.5f} y la de sacar 33 como {prob_E33:.5f}.')