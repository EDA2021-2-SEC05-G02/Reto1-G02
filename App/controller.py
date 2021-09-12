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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadArtwork(catalog)
    #sortArtist(catalog)
    

def loadArtwork(catalog):
    """
    Carga los archivos de las obras de arte y se agrega a la lista de obras de arte
    """
    Artworkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(Artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


def loadArtist(catalog):
    """
    Carga los archivos de loas artistas y se agrega a la lista de autores
    """
    Artistfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

# Funciones de ordenamiento

def sortArtworksByDA(catalog, size, orden):
    return model.sortArtworksByDA(catalog, size, orden)


# Funciones de consulta sobre el catálogo
def getLast(catalog, num):
    """
    Retorna los últimos num artistas
    """
    return model.getLast(catalog, num)

def getFirts(catalog, num):
    """
    Retorna los últimos num obras de arte
    """
    return model.getFirts(catalog, num)

def getCronologicalArtist (catalog, beginDate, endDate, Sort_Type):
    """
    Retorna los artistas en orden cronologico
    """
    return model.getCronologicalArtist (catalog, beginDate, endDate, Sort_Type)

def getCronologicalArtwork (catalog, beginDate, endDate, Sort_Type):
    """
    Retorna los artistas en orden cronologico
    """
    return model.getCronologicalArtwork (catalog, beginDate, endDate, Sort_Type)

def getArtworksPurchased (catalog):
    return model.getArtworksPurchased(catalog)

def getArtworkTecnique(catalog, artist):
    """
    Retorna las obras de un artista por tecnica
    """
    return model.getArtworkTecnique(catalog, artist)

def getArtworkNationality(catalog):
    """
    Retorna las obras por nacionalidad de los artistas
    """
    return model.getArtworkNationality(catalog)

def changeDateUnknown(catalog):
    return model.changeDateUnknown(catalog)



