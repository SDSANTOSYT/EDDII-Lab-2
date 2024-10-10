import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from model import *

# función para obtener la lista de todos los aeropuertos que serán los nodos del grafo
def airport_node_list() -> dict :
    airports = {}
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        data = list(reader)
        airports = {line[0]: Airport(line[0],line[1],line[2],line[3],line[4],line[5]) for line in data}
        airports.update({line[6]: Airport(line[6],line[7],line[8],line[9],line[10],line[11]) for line in data})
        return airports
 
# función para obtener la lista adyacencia de los aeropuertos que serán los nodos del grafo
def airports_adjacency_list() -> dict:
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        data = list(reader)
        # esta variable es un diccionario que tiene como claves los aeropuertos y de valores una lista de los aeropuertos que son destinos para ese aeropuerto sin repetirse
        airport_connections = {airport: list(set([connection[6] for connection in data if connection[0] == airport and connection[6] != connection[0]] + [connection[0] for connection in data if connection[6] == airport and connection[6] != connection[0]])) for airport in airport_node_list().keys()}
        return airport_connections
    
aeropuertos = airport_node_list()
print(len(aeropuertos.keys()))
#print(aeropuertos['NRL'])
conecciones = airports_adjacency_list()
#print(conecciones['NRL'])

grafo = Graph(conecciones,aeropuertos)
print(grafo.n)
print(grafo.m)
arbol = grafo.kruskal()[1]
print(arbol.m)
