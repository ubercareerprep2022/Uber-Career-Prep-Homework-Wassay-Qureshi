class GraphNode():
    def __init__(self, data):
        self.data = data


class GraphWithAdjacencyList():
    #we can assume the graph is undirected
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
        self.AdjacencyList[node] = set()
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

        #Since graph is undirected we add both edges into the adjacency list
        self.AdjacencyList[self.findNode(node1)].add(self.findNode(node2))
        self.AdjacencyList[self.findNode(node2)].add(self.findNode(node1))


    def removeEdge(self, node1, node2):
        if not node1 in self.nodes and not node2 in self.nodes:
            raise ValueError ("Both nodes are not in graph")

        elif not node1 in self.nodes or not node2 in self.nodes:
            raise ValueError ("One node is not in graph")   

        #Since graph is undirected we remove both edges from the adjacency list
        self.AdjacencyList[self.findNode(node1)].remove(self.findNode(node2))
        self.AdjacencyList[self.findNode(node2)].remove(self.findNode(node1))


    def getAdjNodes(self, key):
        if key not in self.nodes:
            raise ValueError ("Key not in graph")

        else:
            adjacent_nodes = set()
            for node in self.AdjacencyList[self.findNode(key)]:
                adjacent_nodes.add(node.data)
                
            return adjacent_nodes


if __name__ == "__main__":
    graph = GraphWithAdjacencyList()
    graph.addNode(1)
    graph.addNode(2)
    graph.addNode(3)
    graph.addNode(4)

#       1 - 2
#       |   |
#       3 - 4

    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(3, 4)
    graph.addEdge(2, 4)

    assert(graph.getAdjNodes(1) == {2, 3})
    assert(graph.getAdjNodes(2) == {1, 4})
    assert(graph.getAdjNodes(3) == {1, 4})
    assert(graph.getAdjNodes(4) == {2, 3})

    graph.removeEdge(1, 2)
    graph.removeEdge(1, 3)
    graph.removeEdge(3, 4)
    graph.removeEdge(2, 4)

    assert(graph.getAdjNodes(1) == set())
    assert(graph.getAdjNodes(2) == set())
    assert(graph.getAdjNodes(3) == set())
    assert(graph.getAdjNodes(4) == set())

    try:
        graph.addNode(1)
    except:
        ValueError

    try:
        graph.removeNode(5)
    except:
        ValueError

    try:
        graph.getAdjNodes(5)
    except:
        ValueError

    try:
        graph.addEdge(5, 1)
    except:
        ValueError

    try:
        graph.removeEdge(5, 6)
    except:
        ValueError
    
    
