import csv
from collections import namedtuple


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, anyo, censo')

def lee_poblaciones(fichero):
    poblaciones = []
    
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        for pais, codigo, anyo, censo in lector:
            anyo = int(anyo)
            censo = int(censo)
            poblacion = RegistroPoblacion(pais, codigo, anyo, censo)
            poblaciones.append(poblacion)
    
    return poblaciones

def calcula_paises(poblaciones):
    res = set()
    for poblacion in poblaciones:
        res.add(poblacion.pais)
    
    return sorted(res)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    res = []

    for poblacion in poblaciones:
        if poblacion.pais == nombre_o_codigo or poblacion.codigo == nombre_o_codigo:
            tupla = (poblacion.anyo, poblacion.censo)
            res.append(tupla)
    
    return res