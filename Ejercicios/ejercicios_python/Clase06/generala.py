# generala.py
import random
from collections import Counter

#%%
# Ejercicio 6.1: Generala servida
def tirar():
    return [random.randint(1,6) for i in range(5)]

def es_generala(tirada):
    for x in tirada:
        if x == tirada[0]:
            check=True
        else:
            check=False
    if check:
        return True
    return False

N=1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida como {prob:.6f}.')

#%%
# Ejercicio 6.2: Generala no necesariamente servida

def mas_comun(lista):
    data=Counter(lista)
    return data.most_common(1)[0][0]

def prob_generala(N):
    G=0
    for i in range(N):
        tirada = tirar()
        cubilete=[]
        new_cubilete=[]
        if es_generala(tirada):
            G+=1
        else:
            for x in tirada:
                if not x == mas_comun(tirada):
                    cubilete.append(x)
            if es_generala(cubilete):
                G+=1
            else:
                for x in cubilete:
                    if not x == mas_comun(cubilete):
                        new_cubilete.append(x)
                if es_generala(new_cubilete):
                    G+=1
                else:
                    pass
    
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala como {prob:.6f}.')

probabilidad_generala = prob_generala(1000000)