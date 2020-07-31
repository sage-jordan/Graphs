"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue 
        queue = Queue()
        # enqueue our start node
        queue.enqueue(starting_vertex)
        # make a set to track visited notes
        visited = set()
        # while queue still has things in it
        while queue.size() > 0:
        ## dq from front of line, this is our current node
            current_node = queue.dequeue()
        ## check if we've visited, if not:
            if current_node not in visited:
        ## mark it as visited
                visited.add(current_node)
                print(current_node)
        ## get it's neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### add to queue
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()
        # push our starting node onto the stack
        stack.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()
        # as long as our stack itsn't empty
        while stack.size() > 0:
        ## pop off the top this is our current node
            current_node = stack.pop()
        # check if we have visited this before, and if not:
            if current_node not in visited:
        ## mark it as visited
                visited.add(current_node)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        ### and add them to our stack
                    stack.push(neighbor)
        return stack

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft_visit(v):
            visited.add(v)
            print(v)
            neighbors = self.get_neighbors(v)
            if len(neighbors) > 0:
                for neighbor in neighbors:
                    if neighbor not in visited:
                        dft_visit(neighbor)

        for v in self.vertices:
            if v not in visited:
                dft_visit(v)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([starting_vertex])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # get all neighbors
            for neighbor in self.get_neighbors(node):
                new_path = list(path) # copy path
                new_path.append(neighbor) # append path with this neighbor
                queue.append(new_path) # enqueue whole path
            


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([starting_vertex])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            print(path)
            node = path[-1]
            print(node)
            # path found
            if node == destination_vertex:
                return path
            # enumerate all neighbor nodes, construct a new path and push it into the queue
            for neighbor in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        if len(path) == 0:
            path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
