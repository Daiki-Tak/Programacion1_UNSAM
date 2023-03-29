# diccionario_geringoso.py

def geringoso(cadena):
  capadepenapa = ''
  for c in cadena:
    capadepenapa+=c
    if c.lower() in ['a','e','i','o','u']:
      replace='p'+c
      capadepenapa+=replace
  return capadepenapa

lista = ['banana', 'manzana', 'mandarina']
d = {}

for i in lista:
  d[i] = geringoso(i)

for k in d:
  print(f'{k} = {d[k]}')
# =============================================================================
# banana = bapanapanapa
# manzana = mapanzapanapa
# mandarina = mapandaparipinapa
# =============================================================================
