from GraphEx1 import GraphNode, GraphWithAdjacencyList
#imported graph class and node from graph ex 1 hw assignment

#did implementations of graph class, one with the nodes and another with a graph with just numbers 
class Graph():
    def __init__(self, nodes = {}):
        self.nodes = nodes

    def addNode(self, node):
        self.nodes[node] = []

    def addEdge(self, node1, node2):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def minNumberOfEdges(self, node1, node2):
        if node1 and node2 not in self.nodes.keys():
            raise ValueError ("node1 and node 2 are not in graph")

        if node1 not in self.nodes.keys():
            raise ValueError ("node1 not in graph")

        if node2 not in self.nodes.keys():
            raise ValueError ("node2 not in graph")

        if node1 == node2:
            return 0
        
        visited = set()
        queue = []
        queue.append([node1])
        
        while queue:

            current_path = queue.pop(0)
            current_node = current_path[-1]
            
            if current_node not in visited:
                visited.add(current_node)

                neighbours = self.nodes[current_node]

                for neighbour in neighbours:

                    if neighbour not in visited:
                        temp = current_path[:]
                        temp.append(neighbour)
                        queue.append(temp)
                    
                    if neighbour == node2:
                        return len(temp) - 1
                        

        raise ValueError ("No Path exists")


class Graph2(GraphWithAdjacencyList):
    def minNumberOfEdges(self, node1, node2):
        if node1 and node2 not in self.nodes:
            raise ValueError ("node1 and node 2 are not in graph")

        if node1 not in self.nodes:
            raise ValueError ("node1 not in graph")

        if node2 not in self.nodes:
            raise ValueError ("node2 not in graph")

        if node1 == node2:
            return 0
        
        visited = set()
        queue = []
        queue.append([self.findNode(node1)])
        
        while queue:

            current_path = queue.pop(0)
            current_node = current_path[-1]
            
            
            if current_node not in visited:
                visited.add(current_node)

                neighbours = self.AdjacencyList[current_node]

                for neighbour in neighbours:

                    if neighbour not in visited:
                        temp = current_path[:]
                        temp.append(neighbour)
                        queue.append(temp)
                    
                    if neighbour.data == node2:
                        return len(temp) - 1
                        
                        

        raise ValueError ("No Path exists")

if __name__ == "__main__":
    graph1 = Graph()
    graph1.addNode(1)
    graph1.addNode(2)
    graph1.addNode(3)
    graph1.addNode(4)
    graph1.addNode(5)
    graph1.addNode(6)

#   1: 2, 3, 4
#   2: 1, 4
#   3: 1, 5
#   4: 1, 2, 5, 6
#   5: 3, 4, 6
#   6: 4, 5

#       1 - 2
#       | \ |
#       3   4
#       | / |
#       5 - 6

    graph1.addEdge(1, 2)
    graph1.addEdge(1, 3)
    graph1.addEdge(1, 4)
    graph1.addEdge(2, 4)
    graph1.addEdge(3, 5)
    graph1.addEdge(4, 6)
    graph1.addEdge(4, 5)
    graph1.addEdge(5, 6)

#shortest path from 1 to 6 is 2 (from 1 to 4 then 4 to 6)

    assert(graph1.minNumberOfEdges(1, 6) == 2)
    assert(graph1.minNumberOfEdges(1, 4) == 1)
    assert(graph1.minNumberOfEdges(6, 3) == 2)
    assert(graph1.minNumberOfEdges(3, 4) == 2)

    
    graph2 = Graph2()
    graph2.addNode(1)
    graph2.addNode(2)
    graph2.addNode(3)
    graph2.addNode(4)
    graph2.addNode(5)
    graph2.addNode(6)

#   1: 2, 3, 4
#   2: 1, 4
#   3: 1, 5
#   4: 1, 2, 5, 6
#   5: 3, 4, 6
#   6: 4, 5

#       1 - 2
#       | \ |
#       3   4
#       | / |
#       5 - 6

    graph2.addEdge(1, 2)
    graph2.addEdge(1, 3)
    graph2.addEdge(1, 4)
    graph2.addEdge(2, 4)
    graph2.addEdge(3, 5)
    graph2.addEdge(4, 6)
    graph2.addEdge(4, 5)
    graph2.addEdge(5, 6)

#shortest path from 1 to 6 is 2 (from 1 to 4 then 4 to 6)
#both implementations give the same correct answer

    assert(graph2.minNumberOfEdges(1, 6) == 2)
    assert(graph2.minNumberOfEdges(1, 4) == 1)
    assert(graph2.minNumberOfEdges(6, 3) == 2)
    assert(graph2.minNumberOfEdges(3, 4) == 2)

