from functools import reduce
import random
import os

def cadenaMatriz(data):
        matriz = list(map(list, map(str.strip, data.split('\n') )))
        return matriz

def read_map(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    map_data = reduce(lambda x, y: x + y, lines)
    return map_data


path_completo = f"{'mapas'}/{random.choice( os.listdir('./mapas') )}"

mapa_str = read_map(path_completo)
print(' parte 1')
print(mapa_str)
mapa_matriz = cadenaMatriz(mapa_str)
print(' parte 2 ')
print(mapa_matriz)