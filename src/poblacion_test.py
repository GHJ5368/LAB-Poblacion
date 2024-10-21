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



if __name__ == "__main__":
    fichero = "LAB-Poblacion\data\population.csv"
    poblaciones = test_lee_poblaciones(fichero)
    test_calcula_paises(poblaciones)
    #test_filtra_por_pais(poblaciones, "ESP")