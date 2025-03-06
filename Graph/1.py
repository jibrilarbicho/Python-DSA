class Graph:
    def __init__(self,edges):
        self.dict={}
        for node,edge in edges:
            if node in self.dict:
                self.dict[node].append(edge)
            else:

               self.dict[node] =[edge]
    def bfs(self,start,end):
        queue=[[start]]
        while queue:
            path=queue.pop(0)
            if end==path[-1]:
                return path
            for adjecent in self.dict[path[-1]]:
                newpath=list(path)
                newpath.append(adjecent)
                queue.append(newpath)

        

        
routes = [ 
("Mumbai", "Paris"), 
("Mumbai", "Dubai"), 
("Paris", "Dubai"), 
("Paris", "New York"), 
("Dubai", "New York"), 
("New York", "Toronto"), 
]
graph=Graph(routes)
print(graph.dict)
print(graph.bfs("Mumbai","Toronto"))





