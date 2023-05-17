# -*- coding: utf-8 -*-

def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

str_numeros = input("Ingrese una lista de números separados por comas: ")
numeros = [int(n) for n in str_numeros.split(",")]

pares, impares = contar_pares_impares(numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

# Función contar_pares_impares:
# La funcion recibe una lista de numeros y por cada numero en dicha lista analiza si es par o impar y lo agrega a la lista correspondiente. Luego devuelve las listas impares, pares.
# El primer error que detecté es un error sintáctico (marcado automáticamente por el editor) en la línea 7:
# =============================================================================
# if numero % 2 = 0:
# =============================================================================
# Lo corregí cambiandolo por la siguiente línea
# =============================================================================
# if numero % 2 == 0:
# =============================================================================
# El segundo error podría ser semántico, más que nada en cómo está planteada la función:
# La función se llama *contar* pares e impares, por lo tanto asumo que lo que quiere devolver es la cantidad de números pares e impares que encontró en la lista, en vez de dos listas con los números que fue encontrando.
# Mi solución a esto fue cambiar las variables pares e impares por contadores enteros, y reemplazar las líneas 8 y 10 para que agreguen 1 a su respectivo contador. Además en la línea de retorno (11) devuelve primero impares y luego pares lo cual es confuso porque la función se llama pares e impares, así que los invertí, quedando la función de la siguiente manera:
# =============================================================================
# def contar_pares_impares(numeros):
#     pares = 0
#     impares = 0
#     for numero in numeros:
#         if numero % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
#     return pares, impares
# =============================================================================
# Ya que la función ahora efectivamente retorna la *cantidad* de pares e impares que encontró, en las líneas 17 y 18 dejé diréctamente las variables.