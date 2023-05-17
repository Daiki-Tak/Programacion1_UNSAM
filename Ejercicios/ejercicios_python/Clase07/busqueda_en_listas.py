# busqueda_en_listas.py

def busqueda_lineal_lordenada(lista, e):
    '''Precondición: la lista está ordenada.
    Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for i, z in enumerate(lista):  # recorremos los elementos de la lista
        if z > e:    # si el elemento es mayor a e no está en la lista, 
            break    # salimos del ciclo
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos