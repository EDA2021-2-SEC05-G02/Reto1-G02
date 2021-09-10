"""
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
assert cf
from datetime import datetime, date

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de Obras de arte.
    """
    catalog = {'Artwork': None,
               'Artist': None}

    catalog['Artwork'] = lt.newList('SINGLE_LINKED')
    catalog['Artist'] = lt.newList('SINGLE_LINKED',
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
    artist['ConstituentID'] = int(ConstituentID.replace('[', '').replace(']',''))
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    artist['Gender'] = Gender
    artist['BeginDate'] = int(BeginDate)
    artist['EndDate'] = int(EndDate)
    artist['Wiki QID'] = WikiQID
    artist['ULAN'] = ULAN
    return artist

def newArtwork (ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine,
                AccessionNumber, Classification, Department, DateAcquired, Cataloged,
                URL):
    artwork = {'ObjectID': None, 'Title': "", 'ConstituentID': None,
                'Date': "", 'Medium': "", 'Dimensions': "", 'CreditLine': "", 
                'AccessionNumber': None, 'Classification': "", 
                'Department': "", 'Date Acquired': "", 'Cataloged': "",
                'URL': ""}

    constID_str = ConstituentID.replace('[', '').replace(']','').split(",")
    constID_int = [int(x) for x in constID_str]

    artwork['ObjectID'] = int(ObjectID.replace('[', '').replace(']',''))
    artwork['Title'] = Title
    artwork['ConstituentID'] = constID_int
    artwork['Date'] = Date
    artwork['Medium'] = Medium
    artwork['Dimensions'] = Dimensions
    artwork['CreditLine'] = CreditLine
    artwork['AccessionNumber'] = AccessionNumber
    artwork['Classification'] = Classification
    artwork['Department'] = Department
    if DateAcquired != "":
        artwork['Date Acquired'] = datetime.strptime(str(DateAcquired), '%Y-%m-%d').date()
    artwork['Cataloged'] = Cataloged
    artwork['URL'] = URL
    return artwork
    
# Funciones de consulta
def getLast3Atworks(catalog):
    atw = catalog['Artwork']
    lastres = lt.newList('SINGLE_LINKED')
    for i in range(lt.size(atw)-2,lt.size(atw)+1):
        last = lt.getElement(atw, i)
        lt.addLast(lastres, last)
    return lastres

def getLast3Artists(catalog):
    at = catalog['Artist']
    lastres = lt.newList('SINGLE_LINKED')
    for i in range(lt.size(at)-2,lt.size(at)+1):
        last = lt.getElement(at, i)
        lt.addLast(lastres, last)
    return lastres

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartist (authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def compareDates(Artist1, Artist2):
    return (int(Artist1['BeginDate']) > int(Artist2['BeginDate']))

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    if artwork1['Date Acquired'] < artwork2['Date Acquired']:
        return True
    else:
        return False

# Funciones de ordenamiento

def sortArtist(catalog):
    sa.sort(catalog['Artist'], compareDates)
