
from .airport import *

class Graph:
    
    def __init__(self, adjacency_list: dict, node_list: dict[str, Airport]) -> None:
        self.L = adjacency_list
        self.n = len(self.L)
        self.airports = node_list
        self.weight_matrix = self.calculate_weight_matrix()
        
    def calculate_weight_matrix(self):
        weight_matrix = {node: {node1: 0 if node1 not in self.L[node] else self.airports[node].haversine(self.airports[node1]) for node1 in self.L.keys()  } for node in self.L.keys()}
        return weight_matrix
    