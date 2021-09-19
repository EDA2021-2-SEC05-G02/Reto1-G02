﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qui
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf
import datetime as dt
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo de Obras de arte.
    """
    catalog = {'Artwork': None,
               'Artist': None}

    catalog['Artwork'] = lt.newList(tipo)
    catalog['Artist'] = lt.newList(tipo,
                                    cmpfunction=compareartist)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    a = newArtwork(artwork['ObjectID'],artwork['Title'],artwork['ConstituentID'],
                    artwork['Date'],artwork['Medium'],artwork['Dimensions'],
                    artwork['CreditLine'],artwork['AccessionNumber'],artwork['Classification'],
                    artwork['Department'],artwork['DateAcquired'],artwork['Cataloged'],
                    artwork['URL'],)

    lt.addLast(catalog['Artwork'], a)


def addArtist(catalog, artist):
    a = newArtist(artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'],
                    artist['Nationality'], artist['Gender'], artist['BeginDate'], 
                    artist['EndDate'], artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['Artist'], a)


# Funciones para creacion de datos

def newArtist(ConstituentID, DisplayName, ArtistBio, Nationality, Gender,
                BeginDate, EndDate, WikiQID, ULAN):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {'ConstituentID': None, 'DisplayName': "", 'ArtistBio': "",
                'Nationality': "", 'Gender': "", 'BeginDate': None, 
                'EndDate': None, 'Wiki QID': "", 'ULAN': ""}
    artist['ConstituentID'] = int(ConstituentID)
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    if Nationality == "":
        artist['Nationality'] = "Unknown"
    artist['Gender'] = Gender
    if Gender == "":
        artist['Gender'] = "Unknown"
    artist['BeginDate'] = int(BeginDate)
    artist['EndDate'] = int(EndDate)
    artist['Wiki QID'] = WikiQID
    if WikiQID == "":
        artist['Wiki QID'] = "Unknown"
    artist['ULAN'] = ULAN
    if ULAN == "":
        artist['ULAN'] = "Unknown"
    
    return artist

def newArtwork (ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine,
                AccessionNumber, Classification, Department, DateAcquired, Cataloged,
                URL):
    artwork = {'ObjectID': None, 'Title': None, 'ConstituentID': None,
                'Date': None, 'Medium': None, 'Dimensions': None, 'CreditLine': None, 
                'AccessionNumber': None, 'Classification': None, 
                'Department': None, 'Date Acquired': None, 'Cataloged': None,
                'URL': None}

    constID_str = ConstituentID.replace('[', '').replace(']','').split(",")
    constID_int = [int(x) for x in constID_str]

    artwork['ObjectID'] = int(ObjectID.replace('[', '').replace(']',''))
    artwork['Title'] = Title
    artwork['ConstituentID'] = constID_int
    artwork['Date'] = Date
    artwork['Medium'] = Medium
    if Medium == "":
        artwork['Medium'] = "Unknown"
    artwork['Dimensions'] = Dimensions
    if Dimensions == "":
        artwork['Dimensions'] = "Unknown"
    artwork['CreditLine'] = CreditLine
    artwork['AccessionNumber'] = AccessionNumber
    artwork['Classification'] = Classification
    artwork['Department'] = Department
    if DateAcquired != "":
        date = DateAcquired.split("-")
        artwork['Date Acquired'] = dt.date(int(date[0]),int(date[1]),int(date[2]))
    else:
        artwork['Date Acquired'] = dt.date(1,1,1)
    artwork['Cataloged'] = Cataloged
    artwork['URL'] = URL
    if URL == "":
        artwork['URL'] = "Unknown"
    return artwork

# Funciones de consulta
def getFirts(catalog, num):
    first = lt.newList('SINGLE_LINKED')
    rangmax = num +1
    for i in range(1, rangmax):
        element = lt.getElement(catalog, i)
        lt.addLast(first, element)
    return first

def getLast(catalog, num):
    last = lt.newList('SINGLE_LINKED')
    rangmin = num-1
    for i in range((lt.size(catalog)-rangmin),lt.size(catalog)+1):
        element = lt.getElement(catalog, i)
        lt.addLast(last, element)
    return last

def getCronologicalArtist (catalog, beginDate, endDate, Sort_Type):
    Artists = catalog['Artist']
    time, ArtistSorted = sortCatalog(Artists, lt.size(Artists), Sort_Type, cmpArtistByBeginDate)
    BornInRange = lt.newList('SINGLE_LINKED')
    for artista in lt.iterator(ArtistSorted):
        if beginDate <= artista['BeginDate'] and endDate >= artista['BeginDate']:
            lt.addLast(BornInRange, artista)
    return time, BornInRange

def getCronologicalArtwork (catalog, beginDate, endDate, Sort_Type):
    Artworks = catalog['Artwork']
    time, ArtworksSorted = sortCatalog(Artworks, lt.size(Artworks), Sort_Type, cmpArtworkByDateAcquired)
    AcquiredInRange = lt.newList('SINGLE_LINKED')
    for artwork in lt.iterator(ArtworksSorted):
        if beginDate <= artwork['Date Acquired'] and endDate >= artwork['Date Acquired']:
            lt.addLast(AcquiredInRange, artwork)
    
    return time, AcquiredInRange

def getArtworksPurchased (catalog):
    purchased = 0
    for item in lt.iterator(catalog):
        if "purchase" in item['CreditLine'].lower():
            purchased += 1
    return purchased

# Funcion 3

def getArtworkTecnique(catalog, artist):
    pass






# Funcion 4

def getArtworkNationality(catalog):

    """
    1. Dic 1: Crear un diccionario para obras {} - Check
    2. Dic 2: Crear un diccionario para artistas {} - Check
    3. Iterar por los artistas - Check
    4. Llenar diccionario id: Valor todo el artista, llave: ConstutentID - Check
    5. Iterar por las obras -Check
    6. Sacar ConstutentID de las obras - Check
    7. Sacar el artista usando el diccionario #2 - Pendiente
    8. Sacar la nacionalidad del Artista - Pendiente
    9. Llenar diccionario #1 con la llave Nacionalidad y Lista de Obras - Pendiente
    9.1 Crear Lista Si la llave no existe el diccionario junto al valor iterado - Pendiente
    9.2 Anadir a Lista si la llave existe - Pendiente
    10. Crear Funcion de Comparacion para Dic 1 
    10.1 Crear Lista de del diccionario para poder organizarla, teniendo en cuenta que las funciones del reto no funcionan con diccionarios
    11. Sortear Dic1 por Longitud de las Obras y Mostrar TOP 10 LLaves - Imcomplete
    12. Mostrar 3 primeros y ultimos 3 artistas con la nacionalidad en el primer lugar - 

    """
    Artists = catalog['Artist']
    Artworks = catalog['Artwork']
    artowrksbynt = {}
    artistsbyid = {}
    const = lt.newList('ARRAY_LIST')
    for item in lt.iterator(Artists):
        artistsbyid[item['ConstituentID']] = item 

    for con in lt.iterator(Artworks):
        lt.addLast(const, con['ConstituentID'])

    return artistsbyid
# Funcion 5
"""
1. Hacer un diccionario o lista para iterar por los departamentos
2. Clasificar las obras por los tamanos kg, m2, m3
2.1 Sacar los valores correspondientes de las obras, del weight y guardarlos en una lista
2.2 Crear una condicion para poder realizar la regla del costo de la obra por cada uno de los elementos de la lista
3. En caso de que no haya informacion del tamano, hacer un else y aplicar una tarifa de 48.00 USD
"""











# Funciones utilizadas para comparar elementos dentro de una lista

def compareartist (authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def cmpArtistByBeginDate(Artist1, Artist2):
    return (int(Artist1['BeginDate']) < int(Artist2['BeginDate']))


def cmpArtworkByDateAcquired(artwork1, artwork2): 
    return artwork1['Date Acquired'] < artwork2['Date Acquired']

# Funciones de ordenamiento

def sortCatalog(catalog, size, Sort_Type, cmp):
    sub_list = lt.subList(catalog, 1, size)
    sub_list = sub_list.copy()
    sorted = None
    start = time.process_time()
    if Sort_Type == 1:
        sorted = qui.sort(sub_list, cmp)
    elif Sort_Type == 2:
        sorted = ins.sort(sub_list, cmp)
    elif Sort_Type == 3:
        sorted = sa.sort(sub_list, cmp)
    elif Sort_Type == 4:
        sorted = mer.sort(sub_list, cmp)
    end = time.process_time()
    time_mseg = (end - start)*1000
    return time_mseg, sorted
