import sys
input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.data = {}
    
    def addEdges(self, u, v):
        self.data[u] = self.data.get(u, []) + [v]
        self.data[v] = self.data.get(v, []) + [u]
    
    def getVertices(self, u):
        return self.data.get(u, [])

graph = Graph()
input()
for i in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        graph.addEdges(arr[1], arr[2])
    
    else:
        print(graph.getVertices(arr[1]))