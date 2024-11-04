import csv
from collections import namedtuple
import matplotlib.pyplot as plt

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

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    res = []
    for p in poblaciones:
        if p.anyo == anyo:
            if p.pais in paises:
                tupla = (p.pais, p.censo)
                res.append(tupla)
    return res

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_anyos = []
    lista_habitantes = []
    for p in poblaciones:
        if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo:
                lista_anyos.append(p.anyo)
                lista_habitantes.append(p.censo)
    
    plt.title(f"Evolucion de la poblacion de {nombre_o_codigo}")
    plt.plot(lista_anyos, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = []
    lista_habitantes = []
    for p in poblaciones:
        if p.anyo == anyo:
            if p.pais in paises:
                lista_paises.append(p.pais)
                lista_habitantes.append(p.censo)
    
    plt.title(f"Comparativa de las poblaciones de {lista_paises} en el año {anyo}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()

