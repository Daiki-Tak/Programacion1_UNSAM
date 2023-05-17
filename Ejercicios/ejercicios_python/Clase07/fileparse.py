# fileparse.py
# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar un subconjunto de las columnas.
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        # Si hay encabezados, los lee 
        if has_headers:
            headers = next(rows)
        # Si hay una seleccion de columnas, las almacena por indices
        if select:
            indexes = [headers.index(nombre_columna) for nombre_columna in select]
            # Si hay encabezados, toma solo los seleccionados
            if has_headers:
                headers = select
        else:
            indexes = []
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indexes: # Si hay una seleccion de columnas, solo utiliza esas
                row = [row[index] for index in indexes]
            if types: # Si hay tipos, los toma en cuenta
                row = [func(val) for func, val in zip(types, row)]
            if has_headers: # Si tiene encabezados, arma diccionarios
                registro = dict(zip(headers, row))
            else: # Caso contrario arma tuplas
                registro = tuple(row)
            registros.append(registro)
    return registros