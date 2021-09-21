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
    print("2- Organizar el catalogo de artistas por fecha de nacimiento")
    print("3- Organizar el catalogo de obras por fecha de adquisicion")
    print("4- Req 1: Listar cronológicamente los artistas")
    print("5- Req 2: Listar cronológicamente las adquisiciones")
    print("6- Req 3: Clasificar obras de un artista por técnica")
    print("7- Req 4: Clasificar obras por la nacionalidad de sus creadores")
    print("8- Req 5: Transportar obras de un departamento")
    print("9- Req 6: Proponer una nueva exposición en el museo")
    

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

def printArtistTable(artist):
    x = PrettyTable()
    x.field_names = ["ConstituentID", "DisplayName",
                    "BeginDate", "Nationality", 
                    "Gender", "ArtistBio", 
                    "Wiki QID", "ULAN"]

    for i in lt.iterator(artist):
        x.add_row([ i["ConstituentID"], i["DisplayName"], 
                    i["BeginDate"], i["Nationality"], 
                    i["Gender"], i["ArtistBio"], 
                    i["Wiki QID"], i["ULAN"]])
    x.align = "l"
    x.align["ConstituentID"] = "r"
    x.align["BeginDate"] = "r"
    print(x)

def printArtworkTable(artwork):
    x = PrettyTable()
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID", "Medium", 
                    "Dimensions", "Date", 
                    "DateAcquired", "URL"]

    x._max_width = {"Title":18,"ConstituentID":18, "Medium":18, "Dimensions":18, "URL":15}

    for i in lt.iterator(artwork):
        if i["Date"] == 5000:
            x.add_row([ i["ObjectID"], i["Title"], 
                        i["ConstituentID"], i["Medium"], 
                        i["Dimensions"], "Unknown", 
                        i["Date Acquired"], i["URL"]])
        else:
            x.add_row([ i["ObjectID"], i["Title"], 
                        i["ConstituentID"], i["Medium"], 
                        i["Dimensions"], i["Date"], 
                        i["Date Acquired"], i["URL"]])
    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r" 
    print(x)

def printMediumTable(artwork, medium):
    x = PrettyTable()
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID", "Medium", 
                    "Dimensions", "Date", 
                    "DateAcquired", "URL"]

    x._max_width = {"Title":18,"ConstituentID":18, "Medium":18, "Dimensions":18, "URL":15}

    for i in lt.iterator(artwork):
        if i["Medium"] == medium:
            if i["Date"] == 5000:
                x.add_row([ i["ObjectID"], i["Title"], 
                            i["ConstituentID"], i["Medium"], 
                            i["Dimensions"], "Unknown", 
                            i["Date Acquired"], i["URL"]])
            else:
                x.add_row([ i["ObjectID"], i["Title"], 
                            i["ConstituentID"], i["Medium"], 
                            i["Dimensions"], i["Date"], 
                            i["Date Acquired"], i["URL"]]) 
            
    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r" 
    print(x)

def printTransCostTable(artwork):
    x = PrettyTable()
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID", "Medium", 
                    "Dimensions", "Date", 
                    "TransCost", "URL"]

    x._max_width = {"Title":18,"ConstituentID":18, "Medium":18, "Dimensions":18, "URL":15}

    for i in lt.iterator(artwork):
        if i["Date"] == 5000:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i["Medium"], 
                    i["Dimensions"], "Unknown", 
                    i["TransCost"], i["URL"]])
        else:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i["Medium"], 
                    i["Dimensions"], i["Date"], 
                    i["TransCost"], i["URL"]])

    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r" 
    print(x)

catalog = None
sortedArtwork_DateA = None
sortedArtwork_Date = None
sortedArtist_BDate = None
DepartmentList = lt.newList()

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
        artist = controller.getLast(catalog['Artist'], 3)
        printArtistTable(artist)

        print("Las últimas 3 obras son: ")
        art = controller.getLast(catalog['Artwork'], 3)
        printArtworkTable(art)

    elif int(inputs[0]) == 2:
        print("Si desea obtener el catalogo de artistas organizado por fecha de nacimiento usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort")
        print("2. Organizar la lista usando Insertionsort")
        print("3. Organizar la lista usando Shellsort")
        print("4. Organizar la lista usando Mergesort")
        orden = int(input('Seleccione una opcion: '))
        if orden not in [1,2,3,4]:
            print("La opcion selecionada no es valida")
        else:
            Artist = catalog['Artist']
            time, sortedArtist_BDate = controller.sortArtistCatalogByBeginDate(Artist, lt.size(Artist), orden)
            print("The time it took to sort the artist catalog with the selected algorithm was:", time ,"mseg\n")

    elif int(inputs[0]) == 3:
        print("Si desea obtener la lista de obras organizada por la fecha de adquision usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort  ")
        print("2. Organizar la lista usando Insertionsort ")
        print("3. Organizar la lista usando Shellsort ")
        print("4. Organizar la lista usando Mergesort ")
        orden = int(input('Seleccione una opcion: '))
        if orden not in [1,2,3,4]:
            print("La opcion selecionada no es valida")
        else:
            Artwork = catalog['Artwork']
            time, sortedArtwork_DateA = controller.sortArtworkCatalogByDateAcquired(Artwork, lt.size(Artwork), orden)
            print("The time it took to sort the artwork catalog with the selected algorithm was:", time ,"mseg\n")


    elif int(inputs[0]) == 4:
        if sortedArtist_BDate == None:
            print("Primero tienes que organizar el catalogo de artistas")
        else:
            beginDate = int(input("Ingrese el año inicial: "))
            endDate = int(input("Ingrese el año final: "))

            print("="*15, " Req No. 1 Inputs ", "="*15)
            print("Artist born between ", beginDate, " and " , endDate, "\n")
            print("="*15, " Req No. 1 Answer ", "="*15)
            ArtistasCrono = controller.getCronologicalArtist(sortedArtist_BDate, beginDate, endDate)
            print("There are ", lt.size(ArtistasCrono), " artist born between", beginDate, " and " , endDate,"\n")

            if lt.size(ArtistasCrono) != 0:
                if lt.size(ArtistasCrono) >= 6:
                    print("The first 3 artist in the range are...")
                    first = controller.getFirts(ArtistasCrono, 3)
                    printArtistTable(first)
                    print("\nThe last 3 artist in the range are...")
                    last = controller.getLast(ArtistasCrono, 3)
                    printArtistTable(last)
                else:
                    print("The artist in the range are...")
                    printArtistTable(ArtistasCrono)

    elif int(inputs[0]) == 5:
        if sortedArtwork_DateA == None:
            print("Primero tienes que organizar el catalogo de obras")
        else:
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
            ObrasCrono = controller.getCronologicalArtwork(sortedArtwork_DateA, first, last)
            purchased = controller.getArtworksPurchased(ObrasCrono)
            print("The MoMA acquired", lt.size(ObrasCrono), "unique pieces between", first, "and" , last)
            print("Of which", purchased, "were purchased\n")
            if lt.size(ObrasCrono)!= 0:
                if lt.size(ObrasCrono) >= 6:
                    print("The first 3 artworks in the range are...")
                    primeros = controller.getFirts(ObrasCrono, 3)
                    printArtworkTable(primeros)

                    print("\nThe last 3 artist in the range are...")  
                    ultimos = controller.getLast(ObrasCrono, 3)
                    printArtworkTable(ultimos)  
                else:
                    print("The artworks in the range are...")
                    printArtworkTable(ObrasCrono)                  

    elif int(inputs[0]) == 6:
        artistName= input("Ingrese el nombre de la/el artista: ")
        artist_info = controller.getArtistInfo(catalog, artistName)
        if artist_info != None:
            Id = artist_info['ConstituentID']
            artworksOfArtist = controller.getArtistsArtwork(catalog, Id)
            Technique, topMedium = controller.getArtistTechnique(artworksOfArtist)
            print("="*15, " Req No. 3 Inputs ", "="*15)
            print("Examine the work of the artist named: "+artistName+"\n")
            print("="*15, " Req No. 3 Answer ", "="*15)
            print(artistName, " with MoMA ID",Id, "has",lt.size(artworksOfArtist), "pieces in her/his name at the museum.")
            if lt.size(artworksOfArtist) != 0:
                print("There are" ,len(Technique), "different mediums/techniques in her/his work.\n")
                x=PrettyTable()
                x.field_names = ["Medium Name", "Count"]
                for i in Technique.keys():
                    x.add_row([i, Technique[i]])
                x.sortby = "Count"
                x.reversesort = True
                if len(Technique) > 5:
                    print("Her/his top 5 Medium/Technique are")
                    print(x.get_string(start=0, end=5))
                else:
                    print("Her/his Medium/Technique are:")
                    print(x)
                print("\nHis/her most used Medium/Technique is:", topMedium , "with", Technique[topMedium], "pieces.")
                
                if Technique[topMedium] >= 3:
                    print("A sample of 3",topMedium,"from the collection are:")
                else:
                    print("The",Technique[topMedium],"works of",topMedium,"from the collection are:")
                printMediumTable(artworksOfArtist, topMedium)

    elif int(inputs[0]) == 7:
        print(controller.getArtworkNationality(catalog))

    elif int(inputs[0]) == 8:
        Artwork = catalog['Artwork']
        sortedArtwork_Date = controller.sortArtworkCatalogByDate(Artwork)

    elif int(inputs[0]) == 9:
        if sortedArtwork_Date == None:
            print("Primero tienes que organizar el catalogo de obras por fecha")
        else:
            departamento = input("Ingrese el nombre del departamento del museo: ")
            ArtworkDepartment = controller.getArworkByDepartment(sortedArtwork_Date, departamento)
            if lt.isPresent(DepartmentList, departamento) == 0:
                ArtworkDepartment = controller.getTransportationCost(ArtworkDepartment)
                lt.addLast(DepartmentList, departamento)
            TotalPriece = controller.getArtworkTotalPriece(ArtworkDepartment)
            Weight = controller.getTotalWeight(ArtworkDepartment)
            older5 = controller.getFirts(ArtworkDepartment, 5)
            sortByCost = controller.sortByTransCost(ArtworkDepartment)
            moreExpensive5 = controller.getFirts(sortByCost, 5)
            print("="*15, " Req No. 5 Inputs ", "="*15)
            print("Estimete the cost to transport all artifacts in " + departamento + " MoMA's Departament")
            print("="*15, " Req No. 3 Answer ", "="*15)
            print("The MoMA is going to transport", lt.size(ArtworkDepartment), "from the",departamento)
            print("REMEMBER! NOT all MoMA's data is complete !!! .... These are estimates.")
            print("Estimated cargo weight (kg):", Weight)
            print("Estimated cargo cost (USD):", TotalPriece)

            print("\nThe TOP 5 most expensive items to transport are:")
            printTransCostTable(moreExpensive5)
            print("\nThe TOP 5 oldest items to transport are:")
            printTransCostTable(older5)
            

        
        
            


    elif int(inputs[0]) == 10:
        print("Implementación en curso, vuelve luego ....")
    
    else:
        sys.exit(0)
sys.exit(0)
