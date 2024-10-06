import csv

# función para obtener la lista de todos los aeropuertos que serán los nodos del grafo
def aeroport_node_list() -> list :
    aeroports = []
    with open('src/flights_final.csv',"r",encoding="utf-8") as dataset:
        reader = csv.reader(dataset)
        next(reader)
        for line in reader:
            if line[0] not in aeroports:
                aeroports.append(line[0])
        return aeroports

aeropuertos = aeroport_node_list()
print(aeropuertos)
print(len(aeropuertos))