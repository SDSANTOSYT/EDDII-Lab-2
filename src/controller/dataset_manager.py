import csv

# función para obtener la lista de todos los aeropuertos que serán los nodos del grafo
def aeroport_node_list() -> dict :
    aeroports = {}
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        aeroports = {line[0]: line[0:6] for line in reader}
            
            #if line[0] not in aeroports:
             #   aeroports.append(line[0])
        return aeroports

def aeroport_edges_list() -> list:
    connections = []
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        connections_1 = list(set([str(f"{line[0]},{line[6]}") for line in reader]))
        connections = [connection for connection in connections_1 if str(f"{connection[4:]},{connection[0:3]}") not in connections ]
        return connections

aeropuertos = aeroport_node_list()
conecciones = aeroport_edges_list()
#print(aeropuertos.keys())
print(len(aeropuertos))
print(len(conecciones))