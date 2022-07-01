class GraphNode():
    def __init__(self, data):
        self.data = data


class GraphWithAdjacencyList():
    #we can assume the graph is directed as the example graph given is directed
    def __init__(self, AdjacencyList = {}, nodes = []):
        self.AdjacencyList = AdjacencyList
        self.nodes = nodes 


    def findNode(self, key):
        #added additional function to help with finding nodes corresponding to keys
        for i in self.AdjacencyList.keys():
            if i.data == key:
                return i


    def addNode(self, key):
        #doesn't allow for duplicates
        if key in self.nodes:
            raise ValueError ("Key already in graph")

        node = GraphNode(key)
        self.AdjacencyList[node] = []
        self.nodes.append(key)


    def removeNode(self, key):
        if not key in self.nodes:
            raise ValueError ("Key not in graph")
        
        del self.AdjacencyList[self.findNode(key)]
        self.nodes.remove(key)


    def addEdge(self, node1, node2):
        if not node1 in self.nodes and not node2 in self.nodes:
            raise ValueError ("Both nodes are not in graph")

        elif not node1 in self.nodes or not node2 in self.nodes:
            raise ValueError ("One node is not in graph")

        self.AdjacencyList[self.findNode(node1)].append(self.findNode(node2))


    def removeEdge(self, node1, node2):
        if not node1 in self.nodes and not node2 in self.nodes:
            raise ValueError ("Both nodes are not in graph")

        elif not node1 in self.nodes or not node2 in self.nodes:
            raise ValueError ("One node is not in graph")   

        self.AdjacencyList[self.findNode(node1)].remove(self.findNode(node2))


    def getAdjNodes(self, key):
        if key not in self.nodes:
            raise ValueError ("Key not in graph")

        else:
            adjacent_nodes = set()
            for node in self.AdjacencyList[self.findNode(key)]:
                adjacent_nodes.add(node.data)
                
            return adjacent_nodes

          
    def DFS(self, key):
        if key not in self.nodes:
            raise ValueError ("Key not in graph")

        stack = []
        stack.append(self.findNode(key))
        visited = set()

        while stack:
            current_node = stack.pop()
            
            if not current_node in visited:
                print(current_node.data, end = " ")
                
            visited.add(current_node)

            if self.AdjacencyList[current_node]:
                for node in self.AdjacencyList[current_node]:
                    if not node in visited:
                        stack.append(node)

                        
    def BFS(self, key):
        if key not in self.nodes:
            raise ValueError ("Key not in graph")

        queue = []
        queue.append(self.findNode(key))
        visited = set()

        while queue:
            current_node = queue.pop(0)
            if not current_node in visited:
                print(current_node.data, end = " ")
                
            visited.add(current_node)

            if self.AdjacencyList[current_node]:
                for node in self.AdjacencyList[current_node]:
                    if not node in visited:
                        queue.append(node)

        

if __name__ == "__main__":
    graph = GraphWithAdjacencyList()
    #constructing graph given in example, cannot draw in comments :(

    graph.addNode(0)
    graph.addNode(1)
    graph.addNode(2)
    graph.addNode(3)

    graph.addEdge(2, 1)
    graph.addEdge(2, 3)
    graph.addEdge(2, 0)

    graph.addEdge(0, 2)
    graph.addEdge(0, 1)

    graph.addEdge(3, 3)

    assert(graph.getAdjNodes(0) == {2, 1})
    assert(graph.getAdjNodes(1) == set())
    assert(graph.getAdjNodes(2) == {0, 1, 3})
    assert(graph.getAdjNodes(3) == {3})

    graph.DFS(2)
    print()
    graph.BFS(2)
