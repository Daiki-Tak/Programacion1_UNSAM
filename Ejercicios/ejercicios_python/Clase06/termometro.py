# termometro.py
import random
import numpy as np

def medir_temp(n):
    temps=[]
    for i in range(n):
        temps.append(random.normalvariate(37.5,0.2))
    saved_temps = np.array(temps)
    np.save('../Data/temperaturas', saved_temps)
    return temps

def resumen_temp(n):
    temps=medir_temp(n)
    maximo=f'{max(temps):.2f}'
    minimo=f'{min(temps):.2f}'
    prom=f'{sum(temps)/n:.2f}'
    sorted(temps)
    if n%2==0:
        pos=int(n/2)
        median=f'{(temps[pos]+temps[pos-1])/2:.2f}'
    else:
        pos=round(n/2)-1
        median=f'{temps[pos]:.2f}'
    # quart1=(temps[n]+1)/4
    # quart3=3*(temps[n]+1)/4
    return (maximo, minimo, prom, median) #(maximo, minimo, prom, quart1, median, quart3)

print(resumen_temp(999))