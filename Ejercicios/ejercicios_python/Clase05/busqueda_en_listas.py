# busqueda_en_listas.py

def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su ultima aparición, de lo
    contrario devuelve -1.
    El algoritmo recorre la lista de atras para adelante y devuelve
    la posicion de la primera aparicion del elemento.
    '''
    pos = -1              # comenzamos suponiendo que e no esta
    i = len(lista) - 1    # inicializo i en la ultima posicion
    while i >= 0:         # recorro la lista de la ultima posicion a la primera
        if lista[i] == e: # si encuentro a e
            pos = i       # guardo su posicion
            break         # y salgo del ciclo
        i-=1
    return pos

# =============================================================================
# >>> buscar_u_elemento([1,2,3,2,3,4],1)
# 0
# >>> buscar_u_elemento([1,2,3,2,3,4],2)
# 3
# >>> buscar_u_elemento([1,2,3,2,3,4],3)
# 4
# >>> buscar_u_elemento([1,2,3,2,3,4],5)
# -1
# =============================================================================

# %%
def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de veces que el elemento e aparece en la
    lista.
    '''
    # n guarda la cantidad de veces que aparece el elemento a medida que recorro la lista.
    n = 0                        # Lo inicializo en 0
    for i,z in enumerate(lista): # Recorro la lista
        if z == e:               # si encuentro a e
            n+=1                 # incremento el contador
    return n

# =============================================================================
# >>> buscar_u_elemento([1,2,3,2,3,4],1)
# 1
# >>> buscar_u_elemento([1,2,3,2,3,4],2)
# 2
# >>> buscar_u_elemento([1,2,3,2,3,4],5)
# 0
# =============================================================================

# %%

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

# =============================================================================
# >>> maximo([4,2,7,2,3,1])
# 7
# >>> maximo([1,2,3,4])
# 4
# >>> maximo([-5,4])
# 4
# >>> maximo([-5,-4])
# -4
# =============================================================================

def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m

# =============================================================================
# >>> minimo([4,2,7,2,3,1])
# 1
# >>> minimo([1,2,3,4])
# 1
# >>> minimo([-5,4])
# -5
# >>> minimo([-4,-5])
# -5
# =============================================================================
