# solucion_de_errores.py
# Ejercicios de errores en el código
# %%
# Ejercicio 3.5: Función tiene_a()
# Comentario: El error es semántico. En un principio, la funcion solo toma en consideración si la palabra posee el caracter 'a', por lo tanto si hay una 'A' presente retornará falso. Por otro lado, en el if, else: esta invertido el orden de prioridades, es decir que en vez de continuar el ciclo para analizar el resto de caracteres, retorna directamente falso si el primer caracter no es una 'a'.
# Lo corregí cambiando la siguiente expresión
# =================================================
#   while i<n:
#       if expression[i] == 'a':
#           return True
#       else:
#           return False
#       i += 1
# =================================================
# Por esta:
# =================================================
#   while i<n:
#       if expression[i].lower() == 'a':
#           return True
#       else:
#           i += 1
#   return False
# =================================================
# De este modo, analiza todos los casos en los que haya una a, tanto minúscula como mayúscula, y devuelve falso únicamente cuando no hay ninguna a. Además me tomé la libertad de agregar un caso extra en el que efectivamente no hay ninguna a, para mostrar que devuelve falso.
# A continuación dejo el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        else:
            i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
print(tiene_a('Crèpes de Tofu'))

# %%

# Ejercicio 3.6: Función tiene_a() parte 2
# Comentario: Hay varios errores: 
# a) Errores sintácticos:
# · En las líneas 1, 4 y 5 falta un ":" al final de la línea;
# · En la línea 8 dice Falso en vez de False.
# b) Error semántico:
# · Igual que en el ejercicio anterior, la expresión no analiza los casos en los que la "a" es mayúscula.
# Para el caso del error semántico, referirse al anterior ejercicio.
# A continuación dejo el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%

# Ejercicio 3.7: Función tiene_uno()
# Comentario: En este ejercicio al ejecutarlo termina con un TypeError ya que la función asume que el input siempre será un string. Para solucionarlo simplemente se puede agregar un paso extra que se asegure de que la expresión sea tratada como un string:
# expresion = str(expresion)
# De esta manera al ejecutar la línea "n = len(expresion)" el output será el esperado.
# A continuación dejo el código corregido:

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

# %%

# Ejercicio 3.8: Funcion suma()
# Comentario: El error aquí es semántico. Dentro de la funcion "suma(a,b)" se declara una variable local c = a + b, pero el valor de c nunca es devuelto, por lo tanto en esencia la función no está realizando ninguna acción. Para solucionarlo debemos agregar un retorno, en este caso "return c".
# A continuación dejo el código corregido:

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# %%
# Ejercicio 3.8: Funcion leer_camion():
# Comentario: El error aca es un poco mas complejo
# Ejercicio 3.8: Función leer_camion():
# Comentario: El error acá es un poco mas complejo: Lo que está sucediendo es que, al declarar el registro fuera de la iteración como un registro vacío y luego referenciarlo en la lista, al modificar el valor de este diccionario también se editará en todas las referencias. 
# Para arreglar este error, lo que hice fue cambiar la manera en la que se define el diccionario para que siempre cree un objeto nuevo por cada iteración y no pise al anterior:
# =============================================================================
# def leer_camion(nombre_archivo):
#     camion=[]
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro = {'nombre': fila[0], 'cajones': int(fila[1]), 'precio': float(fila[2])}
#             camion.append(registro)
#     return camion
# =============================================================================
# A continuación dejo el código corregido:

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {'nombre': fila[0], 'cajones': int(fila[1]), 'precio': float(fila[2])}
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion, sort_dicts=False)