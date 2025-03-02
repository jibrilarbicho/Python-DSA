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
graph=Graph()
graph.AddVertex("A")
graph.AddVertex("B")
graph.AddVertex("C")
graph.AddVertex("D")
graph.Addegde("A","B")
graph.PrintGraph()