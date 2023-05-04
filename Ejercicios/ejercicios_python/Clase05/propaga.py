# propaga.py

def propagar(lista):
    propagada = []
    pivote = -1
    for i,z in enumerate(lista):
        if z==0 and pivote == 1:
            propagada.append(1)
            pivote = 1
        else:
            propagada.append(z)
            pivote = z
    
    i = len(lista) - 1
    while i >= 0:
        if propagada[i]==0 and pivote == 1:
            propagada[i]=1
            pivote = 1
        else:
            pivote = propagada[i]
        i-=1
    return propagada
        

# =============================================================================
# >>> propagar([1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0])
# [1, 1, 1, -1, 0, 0, 0, -1, 0, 0, 0, 0]
# >>> propagar([1, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 1])
# [1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1]
# >>> propagar([0, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, 0])
# [0, 0, 0, -1, 1, 1, 1, -1, 1, 1, 1, 1]
# >>> propagar([0, 0, 1, 0, 0])
# [1, 1, 1, 1, 1]
# >>> propagar([0, 0, 0, 0, 0])
# [0, 0, 0, 0, 0]
# =============================================================================
