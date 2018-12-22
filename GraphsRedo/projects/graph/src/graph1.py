"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Queue(): #FIFO
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None  
    def size(self):
        return len(self.queue)
        
class Stack(): #FILO
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
        
class Vertex: 
    def __init__(self, vertex_id, x = None, y = None, value= None, color = "white"): #you use vertex_id to uniquely identify the vertex. In value, you can have a number, a name, a location, etc 
        #unique id
        self.id = int(vertex_id)
        #value it holds
        self.value = value
        #other vertices the vertex is adjacent to
        self.edges = set()
        self.color = color
        self.x = x
        self.y = y
        
class Graph: 
    """Represent a graph as a dictionary of vertices mapping lables to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1_id, v2_id):
        if self.vertices[v1_id] and self.vertices[v2_id]:
            self.vertices[v1_id].edges.add(self.vertices[v2_id])
            self.vertices[v2_id].edges.add(self.vertices[v1_id])
        else: 
            raise IndexError("That vertex doesn't exist.")
    def add_directed_edge(self, v1_id, v2_id):
        if self.vertices[v1_id] and self.vertices[v2_id]:
            self.vertices[v1_id].edges.add(self.vertices[v2_id])
        else:
            raise IndexError("That vertex doesn't exist")
    
    #DFT (recursion method)
    def dft_recursive(self, start_vert_id, visited = []):
        visited.append(self.vertices[start_vert_id])
        for vertex in self.vertices[start_vert_id].edges:
            if vertex is not None:
                if vertex not in visited:
                    self.dft_recursive(self.vertices[vertex.id].id)
            else:
                pass
        return [vertex.id for vertex in visited]
    
    #DFT (stack method)
    def dft_stack(self, start_vert_id, visited = []):
        stack = Stack()
        stack.push(self.vertices[start_vert_id])
        # while stack.size > 0:
        while len(stack.stack) > 0:
            vertex = stack.pop()
            if vertex in visited:
                pass
            else:
                visited.append(vertex)
                for vertex in self.vertices[vertex.id].edges:
                    if vertex in visited:
                        pass
                    else:
                        stack.push(vertex)
        return [vertex.id for vertex in visited]
    
    #BFT (queue method)
    def bft(self, starting_vert_id):
        visited = []
        queue = Queue()
        queue.enqueue(self.vertices[starting_vert_id])
        while queue.size()>0:
            vertex = queue.dequeue()
            if vertex in visited:
                pass
            else:
                visited.append(vertex)
                for vertex in self.vertices[vertex.id].edges:
                    if vertex in visited:
                        pass
                    else:
                        queue.enqueue(vertex)
        return [vertex.id for vertex in visited]
    
    #DFS(recursion method) + path   --- NOT WORKING. PRINTS PATH BUT DOESNT RETURN IT.
    def dfs_recursive(self,start_vert_id, target_vert_id, visited=[]):
        visited.append(self.vertices[start_vert_id])
        print("visited: ", visited[len(visited)-1].id)
        if self.vertices[start_vert_id].id == target_vert_id:
            print("Target found", [vertex.id for vertex in visited])
            return [vertex.id for vertex in visited]
        for vertex in self.vertices[start_vert_id].edges:
            if vertex is not None:
                if vertex not in visited:
                    self.dfs_recursive(self.vertices[vertex.id].id, target_vert_id)
            else:
                pass
        return [vertex.id for vertex in visited]

    #DFS (stack method) + path
    def dfs_stack(self,start_vert_id, target_vert_id, visited=[], path = []):
        stack = Stack()
        stack.push(self.vertices[start_vert_id])
        while len(stack.stack) > 0:
            vertex = stack.pop()
            if vertex in visited:
                pass
            else:
                visited.append(vertex)
                if vertex.id == target_vert_id:
                    return [vertex.id for vertex in visited]
                else:
                    for vertex in self.vertices[vertex.id].edges:
                        if vertex in visited:
                            pass
                        else:
                            stack.push(vertex)

    #BFS1 (queue method) + path  --- NOT WORKING.
    def bfs1(self, start_vert_id, target_vert_id):
        visited = []
        queue = Queue()
        queue.enqueue(self.vertices[start_vert_id])
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex in visited:
                pass
            else:
                visited.append(vertex)
                if vertex.id == target_vert_id:
                    return [vertex.id for vertex in visited]
                else:
                    for vertex in self.vertices[vertex.id].edges:
                        if vertex in visited:
                            pass
                        else:
                            queue.enqueue(vertex)
        return None
    
    #BFS2 (queue method) + path (Ask Brady about this. Check lecture solution as well.)
    def bfs2(self, start_vert_id, target_vert_id):
        q = Queue()
        q.enqueue([self.vertices[start_vert_id]]) #array gets added to queue
        visited = []
        while q.size() > 0:
            for i in range(0, len(q.queue)):
                print("paths checked: ",[vertex.id for vertex in q.queue[i]]) # prints every path checked before shortest path is found
            path = q.dequeue()
            print("path: ",[vertex.id for vertex in path])
            dequeuedVert = path[-1] 
            print("dequeuedVert: ", dequeuedVert.id)
            if dequeuedVert not in visited:
                if dequeuedVert.id == target_vert_id:
                    return [vertex.id for vertex in path]
                visited.append(dequeuedVert)  # marks vertex as visited
                for next_vert in dequeuedVert.edges: 
                    print("nextVert: ", next_vert.id)
                    new_path = list(path) 
                    new_path.append(next_vert) 
                    print("newPath: ", [vertex.id for vertex in new_path]) 
                    q.enqueue(new_path)
        return None

#Test Code
graph = Graph() 
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)

graph.add_edge(0,1)
graph.add_edge(0,3)
graph.add_edge(1,2)
graph.add_edge(2,5)
graph.add_edge(2,4)
graph.add_edge(4,9)
graph.add_edge(3,7)
graph.add_edge(3,6)
graph.add_edge(7,9)

# print("bft path: ", graph.bft(0)) #works 
# print("dft_stack path: ", graph.dft_stack(0)) #works
# print("dft_recursive path: ", graph.dft_recursive(0)) #works
# print("dfs_stack path: ",graph.dfs_stack(0,7)) #works
# print("dfs_recursive path: ", graph.dfs_recursive(0,7)) #notWorking

# print("bfs1 path: ", graph.bfs1(0,7)) #not working like I want (doesn't return shortest path)
print("bfs2 path2: ", graph.bfs2(0,7))  #working (returns shortest path)