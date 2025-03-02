class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph={}
        for start,end in self.edges:
            if start in  self.graph:
                self.graph[start].append(end)
                pass
            else:
                self.graph[start]=[end]


        



routes = [ 
("Mumbai", "Paris"), 
("Mumbai", "Dubai"), 
("Paris", "Dubai"), 
("Paris", "New York"), 
("Dubai", "New York"), 
("New York", "Toronto"), 
]
route_graph=Graph(routes)
print(route_graph.graph)