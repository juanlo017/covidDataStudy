#-*- coding: utf-8 -*-
'''
Created on 30 nov. 2020

@author: juanq
'''
import csv
from datetime import datetime, date
from collections import namedtuple
from matplotlib import pyplot as plt

'''''
Creamos la namedtuple Registro para que nos sea mas facil identificar los parametros que deseamos usar en las funciones mas adelante.
'''''
Registro = namedtuple('Registro', 'life_expectancy, continent, location, date, total_cases, total_deaths, hospital_beds_per_thousand, gdp_per_capita, population, population_density, median_age, aged_65_older')


##############################################################################
#   2a ENTREGA
##############################################################################

'''''
Lee el fichero y guarda cada linea en una namedtuple tipo Registro que a su vez se guarda en una lista datos.
'''''
def leer_datos(fichero):
    datos = []
    with open(fichero,  encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        
        next(lector)
        
        for life_expectancy, continent, location, date, total_cases, total_deaths, hospital_beds_per_thousand, gdp_per_capita, population, population_density, median_age, aged_65_older  in lector:
            life_expectancy = float(life_expectancy)
            total_cases = float(total_cases) 
            total_deaths = float(total_deaths)
            date = datetime.strptime(date, '%d/%m/%Y').date()
            population = float(population)
            population_density = float(population_density)
            hospital_beds_per_thousand = float(hospital_beds_per_thousand)
            aged_65_older = float(aged_65_older)
            median_age = float(median_age)
            gdp_per_capita = int(gdp_per_capita)
            tupla = Registro(life_expectancy, continent, location, date, total_cases, total_deaths, hospital_beds_per_thousand, gdp_per_capita, population, population_density, median_age,  aged_65_older)
            datos.append(tupla)
    return datos



##############################################################################
#   3a ENTREGA
##############################################################################

#FUNCION 1

'''''
Calcula las muertes totales de una determinada lista de paises y 
en una determinada fecha que les proporcionaremos como parámetros.
ENTRADA:
    - Lista de tuplas tipo Registro. 
    - fecha, fecha que queramos consultar (date).
    - paises, lista de paises que queramos consultar.
SALIDA:
    - Lista de tuplas conteniendo el numero de muertes y el pais correspondientes a ese pais, por cada pais de la 
      lista paises.
'''''
def total_muertes_por_pais_y_fecha(datos, fecha, paises):
    return [(e.location, e.total_deaths) for e in datos if e.date == fecha and e.location in paises]

##########################################################################################################################

#FUNCION 2

'''''
Calcula los todos paises de la base de datos.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - Lista ordenada de los paises(string) presentes en la base de datos
'''''
def calcula_paises(datos):
    return sorted(set(e.location for e in datos) )

##########################################################################################################################

#FUNCION 2.1

'''
Número de paises en el dataset.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - Número de paises presentes en el dataset (integer)
'''
def len_calcula_paises(datos):
    return len(calcula_paises(datos))

##########################################################################################################################

#FUNCION 3

'''
Calcula la poblacion total de todos los paises del dataset sumados para calcular la poblacion mundial.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - Suma (int) de todos los valores unicos de poblacion del dataset (hay 1 dato de poblacion unico por cada pais).

'''
def calcula_poblacion_mundial(datos):
    poblaciones = sorted(set(e.population for e in datos)) 
    total_poblaciones = sum(poblaciones)
    return total_poblaciones

##############################################################################
#   4a ENTREGA
##############################################################################

#FUNCION 4

'''
Calcula la tupla (pais, total_deaths) donde total_deaths sea el mayor de entre 
una lista de tuplas que muestra el pais y las muertes totales en una determinada fecha.
ENTRADA:
    - Lista de tuplas tipo Registro. 
    - fecha, fecha que queramos consultar (date).
    - paises, lista de paises que queramos consultar.
SALIDA:
    - tupla (pais(str), total_deaths(int)).

'''
def mas_muertes_entre_paises_dados(datos, fecha, paises):
    ls = total_muertes_por_pais_y_fecha(datos, fecha, paises)
    return max(ls, key = lambda x : x[1])

##########################################################################################################################

#FUNCION 6

'''''
Calcula los paises que hay en un determinado continente que le pasemos como parámetro. 
--> continentes pueden ser: Europe, North America, Asia, Oceania, South America, Africa.
ENTRADA:
    - Lista de tuplas tipo Registro.
    - Continente(string) que queramos consultar.
SALIDA:
    - Lista de strings de los nombres de paises que pertenecen a ese continente.
'''''
def filtra_por_continente(datos, continente):
    return sorted(set(e.location for e in datos if e.continent == continente) )

##########################################################################################################################

#FUNCION 7

'''
Diccionario en el que las claves son los paises y los valores, una tupla conteniendo: (date, total_deaths). Agrupa por cada pais todas las cifras de muertes junto con el dia en el que se produjeron.
ENTRADA:
    - Lista de tuplas tipo Registro. 
SALIDA:
    - dict {pais(str) : [(date(datetime.date), (total_deaths(int)))]}
'''

def dicc_datos_por_paises(datos):
    res={}
    for i in datos:
        #la clave es el nombre del pais
        clave = i.location
        if clave not in res:
            res[clave] = [(i.date, i.total_deaths)]   
        else:
            l1 = (i.date, i.total_deaths)
            temp = res[clave]
            temp.append(l1)
            res[clave] = temp
    return res

##############################################################################
#   5a ENTREGA
##############################################################################

#FUNCION 8

'''
Calcula un diccionario en el que las claves son los continentes y los valores el numero de paises que hay 
en ese continente.
Toma como entrada unicamente el fichero de datos.
ENTRADA:
    - Lista de tuplas tipo Registro. 
SALIDA:
    - dict {continente(str) : num_paises(int)}
'''
def dicc_contar_paises_por_continente(datos):
    res = dict()
    paises = set() #con esto llevamos nota de los paises que ya hemos contado
    
    for i in datos:
        if i.location not in paises:
            paises.add(i.location) #añadimos el pais a la lista paises
            clave = i.continent 
            if clave not in res:
                res[clave] = 1
            else:
                res[clave] += 1
    return res

##########################################################################################################################

#FUNCION 11

'''
Calcula el nombre del pais donde el porcentaje de poblacion mayor a 65 años afectada
por el coronavirus es más grande.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - Pais con mayor porcentaje de personas mayores de 65 años afectadas (str)
    - porcentaje de mayores afectados
'''
def dicc_pais_con_mas_mayores(datos):
    dicc = dicc_porcentaje_poblacion_mayor_65(datos)
    res = max(dicc.items(), key=lambda x:x[1])
    return res

##########################################################################################################################

#FUNCION 13

'''
Calcula un diccionario donde las claves son el pais y los valores, 
el porcentaje de poblacion mayor a 65 años afectada por el covid.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - dict {pais(str) : porcentaje (float)}
'''
def dicc_porcentaje_poblacion_mayor_65(datos):
    res = dict()
    for i in datos:
        clave = i.location
        porcentaje = (i.aged_65_older/i.population) * 100
        if clave not in res:
            res[clave] = round(porcentaje, 5) #redondeamos a 5 cifras
    return res

##########################################################################################################################

#FUNCION 14

'''
Calcula un diccionario donde las claves son las fechas y los valores una lista de tuplas (pais,muertes) ordenada de mayor a menor en total de muertes ese dia.
ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - dict {pais(str) : porcentaje (float)}
'''

def dicc_top_muertes_por_fecha(datos):
    res={}
    for i in datos:
        clave = i.date
        if clave not in res:
            res[clave] = [(i.location, i.total_deaths)]   
        else:
            l1 = (i.location, i.total_deaths)
            temp = res[clave]
            temp.append(l1)
            res[clave] = sorted(temp, key= lambda x:x[1], reverse=True)[:5]
    return res
##########################################################################################################################

#FUNCION 16
'''
Genera una grafica de muertes por covid frente al tiempo.

ENTRADA:
    - Lista de tuplas tipo Registro.
SALIDA:
    - Grafica
'''
def evolucion_de_muertes_por_pais(datos, pais):
    plt.title('Evolucion de muertes en {} a lo largo del tiempo'.format(pais))
    l_muertes = []
    l_fechas = []
    for i in datos:
        if i.location == pais:
            l_muertes.append(i.total_deaths)
            l_fechas.append(i.date)
    plt.plot(l_fechas, l_muertes)
    plt.show()
    











