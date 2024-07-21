class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
            return True
        return False
    
    def add_edges(self,v1,v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            return True
        return False
    
    def remove_edges(self,v1,v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.graph.keys():
            for other_vertex in self.graph[vertex]:
                self.graph[other_vertex].remove(vertex)
            del self.graph[vertex]
            return True
        return False
    
    def display(self):
        for vertex in self.graph:
            print(vertex,':',self.graph[vertex])
            

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edges('A','B')
g.add_edges('A','C')
g.add_edges('B','C')
g.display()
print('*************************************')
# Removing vetex C
g.remove_vertex('C')
g.display()
print('*************************************')
# Removing vetex 
g.remove_edges('A','D')
g.display()
print('*************************************')
g.add_vertex('C')
g.add_edges('A','C')
g.add_edges('B','C')
g.display()
print('*************************************')
# Removing vetex 
g.remove_edges('A','C')
g.display()
print('*************************************')





