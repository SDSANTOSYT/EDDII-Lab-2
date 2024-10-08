import csv

# función para obtener la lista de todos los aeropuertos que serán los nodos del grafo
def airport_node_list() -> dict :
    airports = {}
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        airports = {line[0]: line[0:6] for line in reader}
        return airports

def airports_adjacency_list() -> dict:
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        data = list(reader)
        # esta variable es un diccionario que tiene como claves los aeropuertos y de valores una lista de los aeropuertos que son destinos para ese aeropuerto sin repetirse
        airport_connections = {airport: list(set([connection[6] for connection in data if connection[0] == airport])) for airport in airport_node_list().keys()}
        for airport in airport_connections:
            for connection in airport_connections[airport]:
                if connection not in airport_connections:
                    airport_connections[connection] = []
        
        for airport in airport_connections:
            for connection in airport_connections[airport]:
                if airport not in airport_connections[connection]:
                    airport_connections[connection].append(airport)
                    airport_connections[connection] = list(set(airport_connections[connection]))
        return airport_connections

def is_directed() -> bool:
    adjacency_list = airports_adjacency_list()
    for airport in adjacency_list:
        for connection in adjacency_list[airport]:
            if airport not in adjacency_list[connection]:
                return True
    
    
aeropuertos = airport_node_list()
conecciones = airports_adjacency_list()

print(len(aeropuertos))
#print(len(conecciones))
print(is_directed())