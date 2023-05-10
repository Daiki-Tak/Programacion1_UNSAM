# generala.py
import random
N=1000000

#%%
# Ejercicio 6.1: Generala servida
def tirar():
    return [random.randint(1,6) for i in range(5)]

def es_generala(tirada):
    '''
    Recibe como parámetro una lista de 5 números entre el 1 y el 6 (tirada de dados)
    y verifica si los 5 números son iguales.
    '''
    return all(x == tirada[0] for x in tirada)

# =============================================================================
# G = sum([es_generala(tirar()) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida como {prob:.6f}.')
# =============================================================================

#%%
# Ejercicio 6.2: Generala no necesariamente servida

def prob_generala(N):
    '''
    Realiza la simulación de un turno entero de Generala para verificar si
    se obtiene una Generala o no.
    '''
    G=0 #inicio el contador para la cantidad de veces que obtuve generala en 0
    for i in range(N): #cada repeticion de este ciclo simula un turno entero
        tiro = tirar() #creo el tiro y lo guardo en una variable local
        if es_generala(tiro): #analizo si ese tiro fue generala
            G+=1
            pass
        #si no se obtuvo generala servida:
        for i in range(2):
            # busco el elemento mas comun del tiro anterior y separo (almaceno) los dados que tengan ese numero
            guardados = [x for x in tiro if x == max(tiro, key=tiro.count)]
            n = 5 - len(guardados)
            # tiro de nuevo los dados que estan en el "cubilete" y genero mi nuevo tiro
            tiro = guardados + [random.randint(1, 6) for _ in range(n)]
            if es_generala(tiro): #analizo si ese tiro fue generala
                G+=1
                break
            #si el tiro no fue generala se repite una vez mas
        #si ninguno de los 3 tiros fue generala se pasa al siguiente turno
    prob = G / N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar una generala como {prob:.6f}.')
    return prob

prob_generala(N)

