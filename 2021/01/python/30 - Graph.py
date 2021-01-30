'''
the following is a work in progress graph code.
i'll post the entire code everytime i make new addition of code with this line at top and 
a what's new section.

what's new:
            printing vertices
            printing edges of particular vertex
            
pending:
            implementation of directed graph
            adding and removing of edges
            adding and removes of vertices
            find adjecent vertices
            error handling for getEdges: vertex = None then asking user to input and call recursively
'''

class graph:
    def __init__ (self,graph_data=None):
        if graph_data is None:
            graph_data = []
        self.graph_dict = graph_data

    def getVertices (self):
        return print(f"Vertices are: {list(self.graph_dict.keys())}")
    
    def getEdges (self, vertex):
        
        if vertex not in list(self.graph_dict.keys()):
            print(f'Vertex {vertex} not found in the graph!')
            return
        print(f"Edges of {vertex}:",end=' ')
        for edges in self.graph_dict[vertex]:
            print(edges,end=' ')
        return

#test code:
g = {1:[2,3,4],2:[1,4],3:[1,2]}

my_g = graph(g)

my_g.getVertices()

my_g.getEdges(2)

my_g.getEdges(4)