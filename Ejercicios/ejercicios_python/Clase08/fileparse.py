# fileparse.py
import csv

def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un objeto iterable en una lista de registros.
    Puede recibir el nombre de un archivo en vez de un iterable.
    Se puede seleccionar un subconjunto de las columnas.
    '''
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    # Si en vez de un iterable se le pasa una cadena, asume que es el nombre de un archivo y lo abre.
    if type(iterable) == str:
        file = open(iterable, 'rt', encoding='utf-8')
        iterable = file
    rows = csv.reader(iterable)
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
    for i, row in enumerate(rows):
        if not row:    # Saltea filas sin datos
            continue
        if indexes: # Si hay una seleccion de columnas, solo utiliza esas
            row = [row[index] for index in indexes]
        if types: # Si hay tipos, los toma en cuenta
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i}: No pude convertir {row}')
                    print(f'Fila {i}: Motivo: {e}')
                continue
        if has_headers: # Si tiene encabezados, arma diccionarios
            registro = dict(zip(headers, row))
        else: # Caso contrario arma tuplas
            registro = tuple(row)
        registros.append(registro)
    return registros
