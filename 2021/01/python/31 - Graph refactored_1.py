'''
the following is a work in progress graph code.
i'll post the entire code everytime i make new addition of code with this line at top and 
a what's new section.

what's new:
            breadth first search
            depth first search
            improved input taking system
            
pending:
            implementation of directed graph
            adding and removing of edges
            adding and removes of vertices
            find adjecent vertices
            error handling for getEdges: vertex = None then asking user to input and call recursively
'''

from collections import defaultdict

class Graph:
    def __init__ (self):
        self.graph = defaultdict(list)
        
    def addEdge(self,v,e):
        self.graph[v].append(e)
        
    def BFS(self,s):
        visiteded = [False] * (max(self.graph)+1)
        
        queue = []
        
        queue.append(s)
        visiteded[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s,end=' ')
            
            for i in self.graph[s]:
                if not visiteded[i]:
                    queue.append(i)
                    visiteded[i] = True
                    
                    
    def BFS(self,s):
        visiteded = set()
        queue = []
        
        queue.append(s)
        visited.add(s)
        
        while queue:
            s = queue.pop(0)
            print(s,end =' ')
            
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    
                    
    def DFSUtil (self,s,visited):
        visited.add(s)
        print(s,end=' ')
        
        for neighbour in self.graph[s]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
                        
            
    
    def DFS (self,s):
        visited = set()
        
        self.DFSUtil(s,visited)


#driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)

print ("\nFollowing is Depth First Traversal"
                  " (starting from vertex 2)")
g.DFS(2)