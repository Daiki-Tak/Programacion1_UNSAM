# esfera.py
import math

def volumen_de_esfera(r):
    volume = (4/3) * math.pi * r**3
    return volume

r = input('Ingrese el radio de la esfera:')

r = int(r)

print('El volumen de la esfera de radio', r, 'es', volumen_de_esfera(r))