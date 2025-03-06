from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def AddEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    def PrintGraph(self):
        for vertex in self.graph:
            print(vertex,":",self.graph[vertex])
    def TopologicalSortuntil(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.TopologicalSortuntil(i,visited,stack)
        stack.insert(0,v)
    def TopologicalSort(self):
        visited=[]
        stack=[]
        for i in list(self.graph):
            if i not in visited:
                self.TopologicalSortuntil(i,visited,stack)
        print(stack)

g=Graph()
g.AddEdge(5,2)
g.AddEdge(5,0)
g.AddEdge(4,0)
g.AddEdge(4,1)
g.AddEdge(2,3)
g.AddEdge(3,1)
g.PrintGraph()
g.TopologicalSort()
