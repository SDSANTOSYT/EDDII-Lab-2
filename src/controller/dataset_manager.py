import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import *
import pandas as pd

dataframe = pd.read_csv('src/flights_final.csv', header = 'infer')
dataframe.drop_duplicates(inplace=True)
data = dataframe.values.tolist()

# función para obtener la lista de todos los aeropuertos que serán los nodos del grafo
def airport_node_list() -> dict :
    airports = {}
    airports = {line[0]: Airport(line[0],line[1],line[2],line[3],line[4],line[5]) for line in data}
    airports.update({line[6]: Airport(line[6],line[7],line[8],line[9],line[10],line[11]) for line in data})
    return airports
   
# función para obtener la lista adyacencia de los aeropuertos que serán los nodos del grafo
def airports_adjacency_list() -> dict:
    airport_connections = {airport: list(set([connection[6] for connection in data if connection[0] == airport and connection[6] != connection[0]] + [connection[0] for connection in data if connection[6] == airport and connection[6] != connection[0]])) for airport in airport_node_list().keys()}
    return airport_connections
    
from time import time
aeropuertos = airport_node_list()

conecciones = airports_adjacency_list()



time1 = time()
grafo = Graph(conecciones,aeropuertos)
print(f"vertices del grafo original: {grafo.n}")
print(f"aristas del grafo original: {grafo.m}")
arbol = grafo.kruskal()
print(f"Componentes del arbol de expansión minima: \n{arbol[0]}")
print(f"vertices del arbol de expansión minima: {arbol[1].n}")
print(f"aristas del arbol de expansión minima: {arbol[1].m}")
print(f"tiempo de ejecucion: {time()-time1}")