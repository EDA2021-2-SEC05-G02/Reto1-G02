"""
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

""" 
Utilizar el siguiente codigo en caso de que se alcance el limite de recursion y mande el 
siguiente error “RecursionError: maximum recursion depth exceeded in 
comparison”
"""
#default_limit = 1000 
#sys.setrecursionlimit(default_limit*10) 

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

def initCatalog():
    """
    Inicializa el catalogo del museo
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los datos del mueso en la estructura de datos
    """
    controller.loadData(catalog)

def last3Artists(catalog):
    """
    Retorna los últimos 3 artistas registrados
    """
    return controller.getLast3Artists(catalog)
     

def last3Atworks(catalog):
    """
    Retorna los últimos 3 obras registradas
    """
    return controller.getLast3Atworks(catalog)

def conologicalArtist (catalog, beginDate, endDate):
    """
    Retorna los artistas en orden cronologico
    """
    return controller.getConologicalArtist(catalog, beginDate, endDate)
    

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
        # Agregar seleccionar opcion
        print("Cargando información de los archivos ....\n")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras de Arte cargadas: ' + str(lt.size(catalog['Artwork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))

        print("\nLos últimos 3 artistas son: ")
        artist = last3Artists(catalog)
        for i in lt.iterator(artist):
            print(i , "\n")

        print("Las últimas 3 obras son: ")
        art=last3Atworks(catalog)
        for i in lt.iterator(art):
            print(i , "\n")
        

    elif int(inputs[0]) == 2:
        beginDate = int(input("Ingrese el año inicial: "))
        endDate = int(input("Ingrese el año final: "))

        print("="*15, " Req No. 1 Inputs ", "="*15)
        print("Artist born between ", beginDate, " and " , endDate, "\n")
        print("="*15, " Req No. 1 Answer ", "="*15)

        ArtistasCrono = conologicalArtist(catalog, beginDate, endDate)
        print("There are ", lt.size(ArtistasCrono), " artist born between", beginDate, " and " , endDate, "\n")
        print("The first and last 3 artist in range are...\n")

        sub_list_first = lt.subList(ArtistasCrono, 1, 3)
        for i in lt.iterator(sub_list_first):
            print(i , "\n")
        
        #sub_list_last = lt.subList(ArtistasCrono, 223, 224)
        #for i in lt.iterator(sub_list_last):
        #    print(i , "\n")


    elif int(inputs[0]) == 3:
        print("Implementación en curso, vuelve luego ....")
        print("Si desea obtener la lista de obras organizada por la fecha de adquision usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Shellsort  ")
        print("2. Organizar la lista usando Mergesort ")
        print("3. Organizar la lista usando Insertionsort ")
        print("4. Organizar la lista usando Quicksort ")
        print('0. Atras')
        orden = int(input('Seleccione una opcion: '))

    
    elif int(inputs[0]) == 4:
        print("Implementación en curso, vuelve luego ....")
    
    elif int(inputs[0]) == 5:
        print("Implementación en curso, vuelve luego ....")

    elif int(inputs[0]) == 6:
        print("Implementación en curso, vuelve luego ....")

    elif int(inputs[0]) == 7:
        print("Implementación en curso, vuelve luego ....")

    else:
        sys.exit(0)
sys.exit(0)
