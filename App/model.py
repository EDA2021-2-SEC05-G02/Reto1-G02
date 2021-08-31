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

    catalog['Artwork'] = lt.newList()
    catalog['Artist'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartist)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    lt.addLast(catalog['Artwork'], artwork)
    artists = artwork['ConstituentID'].split(",")
    

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
    artist = {'ConstituentID': "", 'DisplayName': "", 'ArtistBio': "",
                'Nationality': "", 'Gender': "", 'BeginDate': "", 
                'EndDate': "", 'Wiki QID': "", 'ULAN': ""}
    artist['ConstituentID'] = ConstituentID
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    artist['Gender'] = Gender
    artist['BeginDate'] = BeginDate
    artist['EndDate'] = EndDate
    artist['Wiki QID'] = WikiQID
    artist['ULAN'] = ULAN
    return artist
    
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartist (authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento
