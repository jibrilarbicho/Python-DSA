# class Graph:
#     def __init__(self,edges):
#         self.edges=edges
#         self.graph={}
#         for start,end in self.edges:
#             if start in  self.graph:
#                 self.graph[start].append(end)
#                 pass
#             else:
#                 self.graph[start]=[end]

# routes = [ 
# ("Mumbai", "Paris"), 
# ("Mumbai", "Dubai"), 
# ("Paris", "Dubai"), 
# ("Paris", "New York"), 
# ("Dubai", "New York"), 
# ("New York", "Toronto"), 
# ]
# route_graph=Graph(routes)
# print(route_graph.graph)
class Graph:
    def __init__(self):
        self.graph_dictionary={}
    def AddVertex(self,vertex):
        if vertex not in self.graph_dictionary:
            self.graph_dictionary[vertex]=[]
        else:
            print("Error: Vertex already exists.")
    def Addegde(self,vertex1,vertxe2):
        if vertex1 and vertxe2 in self.graph_dictionary:
            self.graph_dictionary[vertex1].append(vertxe2)
            self.graph_dictionary[vertxe2].append(vertex1)
        else:
            print("Error: One or both vertices are not in the graph.")
    def PrintGraph(self):    
        for vertex in self.graph_dictionary:
            print(vertex,":",self.graph_dictionary[vertex])
    def removeEdge(self,vertex1,vertex2):
        try:
            if vertex2 in self.graph_dictionary[vertex1] and vertex1 in self.graph_dictionary[vertex2]:
                self.graph_dictionary[vertex1].remove(vertex2)
                self.graph_dictionary[vertex2].remove(vertex1)
        except ValueError:
            print("Error: Edge does not exist.")
    def removevertex(self,vertex):
        if vertex in self.graph_dictionary:
            for othervertex in self.graph_dictionary:
                if vertex in self.graph_dictionary[othervertex]:
                    self.graph_dictionary[othervertex].remove(vertex)
            del self.graph_dictionary[vertex]
        else:
            print("Error: Vertex does not exist.")
              
graph=Graph()
graph.AddVertex("A")
graph.AddVertex("B")
graph.AddVertex("C")
graph.AddVertex("D")
graph.AddVertex("E")

graph.Addegde("A","B")
graph.Addegde("A","C")
graph.Addegde("A","D")
graph.Addegde("B","E")
graph.PrintGraph()
graph.removeEdge("A","E")
graph.PrintGraph()
graph.removevertex("A")
print("After removing vertex A")
graph.PrintGraph()

