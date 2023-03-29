# buscar_precios.py
def buscar_precio(fruta):
    f=open('../Data/precios.csv', 'rt')
    try:
        fruta = fruta.lower().capitalize()  
        for line in f:
            row = line.split(',')
            if row[0]==fruta:
                precio=row[1].strip('\n')
        precio = float(precio)    
        print(f'El precio de un cajón de {fruta} es: {precio}')
        f.close()
        
    except:
        print(f'{fruta} no figura en el listado de precios.')

buscar_precio('frambuesa')
# El precio de un cajón de Frambuesa es: 34.35
buscar_precio('Kale')
# Kale no figura en el listado de precios.