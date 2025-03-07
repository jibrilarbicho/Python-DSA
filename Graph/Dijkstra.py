
import heapq
class Edge:
    def __init__(self,start,weight,targetVertex):
        self.weight=weight
        self.start=start
        self.targetVertex=targetVertex
class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjacencyList=[]
        self.minDistance=float('inf')
    def __lt__(self,other):
        return self.minDistance<other.minDistance
    def  add_egde(self,weight,destinationvertex):
        edge=Edge(self,weight,destinationvertex)
        self.adjacencyList.append(edge)
class DijkstraAlgorithm:
    def __init__(self):
        self.heap=[]
    def calculateShortestPath(self,startVertex):
        startVertex.minDistance=0
        heapq.heappush(self.heap,startVertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.adjacencyList:
                start=edge.start
                target=edge.targetVertex
                newDistance=start.minDistance+edge.weight
                if newDistance<target.minDistance:
                    target.minDistance=newDistance
                    target.predecessor=actual_vertex
                    heapq.heappush(self.heap,target)
            actual_vertex.visited=True
    def getShortestPath(self,Vertex):
        print(f"Shortest path to {Vertex.name} is:",Vertex.minDistance)
        while Vertex is not None:
            print(Vertex.name)
            Vertex=Vertex.predecessor

                
        
    

        

Mumbai=Node("Mumbai")
Paris=Node("Paris")
Dubai=Node("Dubai")
NewYork=Node("New York")
Toronto=Node("Toronto")
LasVegas=Node("Las Vegas")
Addis_Ababa=Node("Addis_Ababa")
Kenya=Node("Kenya")
Washington=Node("Washington")
Mumbai.add_egde(5,Dubai)

Mumbai.add_egde(5,Paris)
Paris.add_egde(3,Dubai)
Paris.add_egde(7,NewYork)
Dubai.add_egde(2,NewYork)
Dubai.add_egde(1,Toronto)
NewYork.add_egde(1,Toronto)
NewYork.add_egde(3,LasVegas)
Toronto.add_egde(2,LasVegas)
Toronto.add_egde(4,Addis_Ababa)
LasVegas.add_egde(6,Addis_Ababa)
LasVegas.add_egde(7,Kenya)
Addis_Ababa.add_egde(3,Kenya)
Addis_Ababa.add_egde(5,Washington)
Kenya.add_egde(2,Washington)

dijkstra=DijkstraAlgorithm()
dijkstra.calculateShortestPath(Mumbai)
dijkstra.getShortestPath(Washington)

