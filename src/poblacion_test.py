from poblacion import *

def test_lee_poblaciones(fichero):
    #print(f"Estamos probando la carga de datos de Poblaciones")
    res = lee_poblaciones(fichero)
    #print(f"Tres primeros registros: {res[:3]}")
    #print(f"=======================================")
    #print(f"Tres primeros registros: {res[-3:]}")
    return res

def test_calcula_paises(poblaciones):
    paises = calcula_paises(poblaciones)
    print(paises)

def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    res = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(res)

def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    res = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    print(f"En el año {anyo} estas son las poblaciones de los paises dados: {res}")

def test_muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    muestra_evolucion_poblacion(poblaciones,nombre_o_codigo)

def test_muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    muestra_comparativa_paises_anyo(poblaciones, anyo, paises)


if __name__ == "__main__":
    fichero = "LAB-Poblacion\data\population.csv"
    poblaciones = test_lee_poblaciones(fichero)
    #test_calcula_paises(poblaciones)
    #test_filtra_por_pais(poblaciones, "ESP")
    #test_filtra_por_paises_y_anyo(poblaciones, 1999, ("Spain","United States","Italy"))
    test_muestra_evolucion_poblacion(poblaciones,"Spain")
    test_muestra_comparativa_paises_anyo(poblaciones,1999, ("Spain","United States","Italy"))