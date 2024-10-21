
from .airport import *

class Graph:
    
    # Constructor de la clase grafo que recibe una lista de nodos y una lista de adyacencia=========================================
    def __init__(self, adjacency_list: dict[str,list[str]], node_list: dict[str, Airport]) -> None:
        self.L = adjacency_list
        self.airports = node_list
        self.n = len(self.L.keys())
        self.weight_matrix = self.calculate_weight_matrix()
        self.m = len(self.get_edges())

    # Función para obtener la lista de aristas del grafo============================================================================
    def get_edges(self) -> list[tuple[str,str,float]]:
        edges = []
        for airport in self.L.keys():
            for connection in self.L[airport]:
                if not (connection, airport, self.weight_matrix[airport][connection]) in edges:
                    edges.append((airport, connection, self.weight_matrix[airport][connection]))
        return edges

    # Función para calcular la matriz de pesos del grafo=============================================================================
    def calculate_weight_matrix(self) -> dict[str,dict[str,float]]:
        weight_matrix = {node: {node1: 0 if node1 not in self.L[node] else self.airports[node].haversine(self.airports[node1]) for node1 in self.L.keys()  } for node in self.L.keys()}
        return weight_matrix

    # Método para recorrer el grafo en profundidad==================================================================================
    def DFS(self, u:str) -> None:
        visited = {airport: False for airport in self.L.keys()}
        self.__DFS_visit(u,visited)

    # Recorrido del grafo recursivo que recibe un nodo y un diccionario de nodos visitados==========================================
    def __DFS_visit(self, u:str, visited: dict[str,bool], can_print = True) -> dict[str,bool]:
        visited[u] = True
        if can_print:
            print(u, end= ' --> ')
        for v in self.L[u]:
            if not visited[v]:
                visited = self.__DFS_visit(v,visited,can_print)
        return visited

    # Función para saber si el grafo es conexo======================================================================================
    def is_connected(self) -> bool:
        visited = {airport: False for airport in self.L.keys()}
        visited = self.__DFS_visit(list(self.L.keys())[0], visited, False)
        return all(visited.values())

    # Función para obtener las componentes conexas del grafo junto con la cantidad de vertices que de cada componente===============
    def number_of_components(self) -> dict[str:int]:
        visited = {airport: False for airport in self.L.keys()}
        components = {}
        visited = self.__DFS_visit(list(self.L.keys())[0], visited, False)
        components[list(self.L.keys())[0]] = len([airport for airport in visited.keys() if visited[airport]])
        previous_visited = components[list(self.L.keys())[0]]
        while not all(visited.values()):
            not_visited = [airport for airport in visited.keys() if not visited[airport]]
            visited = self.__DFS_visit(not_visited[0], visited, False)
            components[not_visited[0]] = len([airport for airport in visited.keys() if visited[airport]]) - previous_visited
            previous_visited += components[not_visited[0]]
        return components

    # Función para obtener el árbol de expansión mínima del grafo===================================================================
    def kruskal(self) -> list[dict[str:list], any]:
        edges = self.get_edges()
        edges.sort(key=lambda edge: edge[2])
        adjacency_list_tree = {}
        aux_adj = adjacency_list_tree.copy()
        for edge in edges:
            if  edge[0] not in list(adjacency_list_tree.keys()):
                adjacency_list_tree[edge[0]] = []
            if  edge[1] not in list(adjacency_list_tree.keys()):
                adjacency_list_tree[edge[1]] = []
            adjacency_list_tree[str(edge[1])].append(str(edge[0]))
            adjacency_list_tree[str(edge[0])].append(str(edge[1]))
            if self.__has_cycles(adjacency_list_tree):
                adjacency_list_tree[str(edge[1])].remove(str(edge[0]))
                adjacency_list_tree[str(edge[0])].remove(str(edge[1]))
                
        
        minimum_expansion_tree = Graph(adjacency_list_tree, self.airports)
        return [{component: [minimum_expansion_tree.number_of_components()[component], round(minimum_expansion_tree.weight_of_component()[component],2)] for component in minimum_expansion_tree.number_of_components().keys()}, minimum_expansion_tree]
    
    # Función para saber si el grafo tiene cíclos===================================================================================
    def has_cycles(self) -> bool:
        return self.__has_cycle(self.L)

    # Función para saber si una lista de adyacencia tiene cíclos====================================================================
    def __has_cycles(self, adj_list: dict[str, list[str]]) -> bool:
        def is_cyclic_visit(u: str, visited: dict[str, bool], parent: str) -> bool:
            visited[u] = True
            for v in adj_list[u]:
                if not visited[v]:
                    if is_cyclic_visit(v, visited, u):
                        return True
                elif parent != v:
                    return True
            return False

        visited = {airport: False for airport in adj_list.keys()}
        for airport in adj_list.keys():
            if not visited[airport]:
                if is_cyclic_visit(airport, visited, None):
                    return True
        return False
    
    # Función para obtener el peso de cada componente del grafo=====================================================================
    def weight_of_component(self) -> dict[str:float]:
        components = self.number_of_components()
        for component in components.keys():
            visited = {airport: False for airport in self.L.keys()}
            components[component] = self.__weight_of_component_visit(component, visited, 0)[1]
        return components
    
    # Función para obtener el peso de una componente del grafo======================================================================
    def __weight_of_component_visit(self, u:str, visited: dict[str,bool], weight_total:float) -> list[dict[str:bool], float]:
        visited[u] = True
        for v in self.L[u]:
            if not visited[v]:
                weight_total += self.weight_matrix[u][v]
                visited, weight_total = self.__weight_of_component_visit(v,visited,weight_total)
        return visited, weight_total
    
    # Función para obtener camino minimo =============================================================================
    def dijktra (self, v:str):
        d = {airport: float("inf") for airport in self.L.keys()}
        
        pad = {airport: None for airport in self.L.keys()}
        
        visit = {airport: False for airport in self.L.keys()}
        d[v]=0
        while (not all(visit.values())):
            v = min ({airport: d[airport] for airport in visit.keys() if not visit[airport] }, key= lambda airport: d[airport])
            visit[v] = True
            for airport in self.L[v]: 
                if (d[v]+ self.weight_matrix[v][airport] < d[airport] and  not visit[airport]):
                    d[airport] = d[v] + self.weight_matrix[v][airport]
                    pad[airport] = v 
        
        return d, pad
    
    def tails (self, v: str):
        d, pad = self.dijktra(v)
        visit = {airport: False for airport in self.L.keys()}
        tail = []
        for i in range (10):
            v1 = max ({airport: d[airport] for airport in visit.keys() if (not visit[airport]) and d[airport] != float("inf")}, key= lambda airport: d[airport])
            tail.append((v1,d[v1]))
            visit[v1] = True
        return tail

    def path(self, u: str, v:str ):
        d, pad = self.dijktra(u)
        path = [v]
        v1 = v
        while (v1 != u):
            v1 = pad[v1]
            path.append(v1)
        path.reverse()
        return path 
        