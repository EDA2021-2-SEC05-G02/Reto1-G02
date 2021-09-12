﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import datetime as dt
from prettytable import PrettyTable

""" 
Utilizar el siguiente codigo en caso de que se alcance el limite de recursion y mande el 
siguiente error “RecursionError: maximum recursion depth exceeded in 
comparison”
"""
default_limit = 1000 
sys.setrecursionlimit(default_limit*100) 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar obras de un artista por técnica")
    print("5- Clasificar obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("8- Lab4 - Elige el tamaño de la muestra de adquisiciones que se va ordenar cronológicamente")
def initCatalog(tipo):
    """
    Inicializa el catalogo del museo
    """
    return controller.initCatalog(tipo)

def loadData(catalog):
    """
    Carga los datos del mueso en la estructura de datos
    """
    controller.loadData(catalog)

def last3(catalog):
    """
    Retorna los últimos 3 artistas registrados
    """
    return controller.getLast3(catalog)
     

def first3(catalog):
    """
    Retorna los últimos 3 obras registradas
    """
    return controller.getFirts3(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Si desea mostrar el catalogo usando un tipo especifico de lista, observe las opciones a continuacion:')
        print('1. Obtener el catalogo utilizando listas tipo SINGLE_LINKED')
        print('2. Obtener el catalogo utilizando listas tipo ARRAY_LIST')

        inp = input('Selecione una opción para continuar: ')
        print("Cargando información de los archivos ....\n")
        if int(inp) == 1:
            catalog = initCatalog('SINGLE_LINKED')
        else:
            catalog = initCatalog('ARRAY_LIST')
        loadData(catalog)
        
        print('Obras de Arte cargadas: ' + str(lt.size(catalog['Artwork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))

        print("\nLos últimos 3 artistas son: ")
        artist = last3(catalog['Artist'])
        for i in lt.iterator(artist):
            print(i , "\n")
            
            

        print("Las últimas 3 obras son: ")
        art=last3(catalog['Artwork'])
        for i in lt.iterator(art):
            print(i , "\n")
        

    elif int(inputs[0]) == 2:
        print("Si desea obtener la lista de obras organizada por la fecha de adquision usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort")
        print("2. Organizar la lista usando Insertionsort")
        print("3. Organizar la lista usando Shellsort")
        print("4. Organizar la lista usando Mergesort")
        orden = int(input('Seleccione una opcion: '))
        if orden in [1,2,3,4]:
            beginDate = int(input("Ingrese el año inicial: "))
            endDate = int(input("Ingrese el año final: "))

            print("="*15, " Req No. 1 Inputs ", "="*15)
            print("Artist born between ", beginDate, " and " , endDate, "\n")
            print("="*15, " Req No. 1 Answer ", "="*15)

            time, ArtistasCrono = controller.getCronologicalArtist(catalog, beginDate, endDate, orden)
            print("The time it took to sort the artist catalog with the selected algorithm was:", time ,"mseg\n")
            print("There are ", lt.size(ArtistasCrono), " artist born between", beginDate, " and " , endDate)
            print("The first and last 3 artist in the range are...\n")
            
            x = PrettyTable()
            x.field_names = ["ConstituentID", "DisplayName", "BeginDate", "Nationality", "Gender", "ArtistBio", "Wiki QID", "ULAN"]
            first = first3(ArtistasCrono)
            for i in lt.iterator(first):
                x.add_row([ i["ConstituentID"], i["DisplayName"], i["BeginDate"], i["Nationality"], i["Gender"], i["ArtistBio"], i["Wiki QID"], i["ULAN"]])
            
            last = last3(ArtistasCrono)
            for i in lt.iterator(last):
                x.add_row([ i["ConstituentID"], i["DisplayName"], i["BeginDate"], i["Nationality"], i["Gender"], i["ArtistBio"], i["Wiki QID"], i["ULAN"]])
            
            x.align = "l"
            x.align["ConstituentID"] = "r"
            x.align["BeginDate"] = "r"            
            print(x)
                
        else:
            print('La opción seleccionada no es valida ....')


    elif int(inputs[0]) == 3:
        print("Si desea obtener la lista de obras organizada por la fecha de adquision usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort  ")
        print("2. Organizar la lista usando Insertionsort ")
        print("3. Organizar la lista usando Shellsort ")
        print("4. Organizar la lista usando Mergesort ")
        orden = int(input('Seleccione una opcion: '))
        if orden in [1,2,3,4]:
            firstY=int(input("Año incial: "))
            firstM=int(input("Mes incial: "))
            firstD=int(input("Dia inicial: "))
            first=dt.date(firstY,firstM,firstD)

            lastY=int(input("Año final: "))
            lastM=int(input("Mes final: "))
            lastD=int(input("Dia final: "))
            last=dt.date(lastY,lastM,lastD)

            print("="*15, " Req No. 2 Inputs ", "="*15)
            print("Artwork aquired between "+ str(first)+" and " +str(last)+ "\n")
            print("="*15, " Req No. 2 Answer ", "="*15)
            time, ObrasCrono = controller.getCronologicalArtwork(catalog, first, last, orden)
            purchased = controller.getArtworksPurchased(ObrasCrono)
            print("The time it took to sort the artwork catalog with the selected algorithm was:", time ,"mseg\n")
            print("The MoMA acquired", lt.size(ObrasCrono), "unique pieces between", first, "and" , last)
            print("With", "---" , "different artist and purchased", purchased, "of them")
            print("The first and last 3 artworks in the range are...\n")

            primeros = first3(ObrasCrono)
            for i in lt.iterator(primeros):
                print(i , "\n")
        
            ultimos = last3(ObrasCrono)
            for i in lt.iterator(ultimos):
                print(i , "\n")
        else:
            print('La opción seleccionada no es valida ....')

            
    elif int(inputs[0]) == 4:
        print("Implementación en curso, vuelve luego ....")

        
    
    elif int(inputs[0]) == 5:
        print("Implementación en curso, vuelve luego ....")

    elif int(inputs[0]) == 6:
        print("Implementación en curso, vuelve luego ....")

    elif int(inputs[0]) == 7:
        print("Implementación en curso, vuelve luego ....")
    
    elif int(inputs[0]) == 8:
        print("Si desea obtener la lista de obras organizada por la fecha de adquision usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort  ")
        print("2. Organizar la lista usando Insertionsort ")
        print("3. Organizar la lista usando Shellsort ")
        print("4. Organizar la lista usando Mergesort ")
        orden = int(input('Seleccione una opcion: '))
        if orden in [1,2,3,4]:
            sizeTotal = lt.size(catalog['Artwork'])
            size = int(input("Indique tamaño de la muestra: "))
            if size <= sizeTotal:
                time, muestraSorted = controller.sortArtworksByDA(catalog['Artwork'], size, orden)
                print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(time))

    else:
        sys.exit(0)
sys.exit(0)
