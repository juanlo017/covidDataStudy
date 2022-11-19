#-*- coding: utf-8 -*-
'''
Created on 30 nov. 2020

@author: juanq
'''

from funciones import *

##############################################################################
#   TEST DE FUNCIONES
##############################################################################

def test_calcula_paises(datos):
    print("TEST de calcula_paises: ")
    res = calcula_paises(datos)
    print('    - Paises: {}'.format(res))

def test_len_calcula_paises(datos):
    print("TEST de len_calcula_paises: ")
    res = len_calcula_paises(datos)
    print('    - Número de Paises: {}'.format(res))

def test_filtra_por_continente(datos):
    continente = 'Europe'
    print("TEST de calcula_poblacion_mundial: ")
    res = filtra_por_continente(datos, continente)
    print('    - Paises pertenecientes a {}: {}'.format(continente, res))

def test_total_muertes_por_pais_y_fecha(datos):
    print("TEST de muertes_por_pais_y_fecha: ")
    paises = ('Germany','Spain')
    #CADA NUMERO DE LA FECHA TIENE QUE TENER 2 DIGITOS SEPARADOS POR UNA BARRA ADELANTE '/'. 
    year, month, day = 2020, 7, 30
    fecha = date(int(year),int(month),int(day)) 
    res = total_muertes_por_pais_y_fecha(datos, fecha, paises)
    print('    - Muertes a dia de {}: {}'.format(fecha, res))

def test_calcula_poblacion_mundial(datos):
    print("TEST de calcula_poblacion_mundial: ")
    res = calcula_poblacion_mundial(datos)
    print('    - Población Mundial: {}'.format(res))
  
def test_mas_muertes_entre_paises_dados(datos):
    year, month, day = 2020, 7, 30
    fecha = date(int(year),int(month),int(day)) 
    paises = ('Germany','Spain', 'China', 'Indonesia', 'Liechtenstein')
    res = mas_muertes_entre_paises_dados(datos, fecha, paises)
    print('TEST de mas_muertesentre_paises_dados: ')
    print('El dia {} murieron {} personas en {}, siendo la mayor tasa de muertes de entre {}'.format(fecha, res[1], res[0], paises))

def test_dicc_datos_por_paises(datos):
    print('TEST de datos_por_paises: ')
    res = dicc_datos_por_paises(datos)
    print('Imprimiendo diccionario: {}'.format(res))

def test_dicc_contar_paises_por_continente(datos):
    print('TEST de contar_paises_por_continente')
    res = dicc_contar_paises_por_continente(datos)
    print('Imprimiendo diccionario: {}'.format(res))

def test_dicc_porcentaje_poblacion_mayor_65(datos):
    print('TEST de porcentaje_poblacion_mayor_65')
    res = dicc_porcentaje_poblacion_mayor_65(datos)
    print('Imprimiendo diccionario: {}'.format(res))

def test_dicc_pais_con_mas_mayores(datos):
    print('TEST de dicc_pais_con_mas_mayores')
    res = dicc_pais_con_mas_mayores(datos)
    print('Imprimiendo diccionario: {}'.format(res))

def test_evolucion_de_muertes_por_pais(datos):
    pais = 'Spain'
    print('TEST de evolucion_de_muertes_por_pais')
    res = evolucion_de_muertes_por_pais(datos, pais)
    print(res)

def test_dicc_top_muertes_por_fecha(datos):
    res = dicc_top_muertes_por_fecha(datos)
    print (res)


################################################################
#  Programa principal
################################################################

datos = leer_datos('data/coviddata3.csv')
print(datos[:5]) #First 5 data rows.    

#test_calcula_paises(datos)

#test_len_calcula_paises(datos)

#test_total_muertes_por_pais_y_fecha(datos)

test_calcula_poblacion_mundial(datos)

test_filtra_por_continente(datos)

test_mas_muertes_entre_paises_dados(datos)

test_dicc_datos_por_paises(datos[29350:29400])

test_dicc_contar_paises_por_continente(datos)

test_dicc_porcentaje_poblacion_mayor_65(datos)

test_dicc_pais_con_mas_mayores(datos)

test_dicc_top_muertes_por_fecha(datos[:2000])

test_evolucion_de_muertes_por_pais(datos)


