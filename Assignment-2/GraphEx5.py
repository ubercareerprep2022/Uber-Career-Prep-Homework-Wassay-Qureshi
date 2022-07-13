class Graph():
    def __init__(self, nodes = {}):
        self.nodes = dict(nodes)

    def addNode(self, node):
        if node in self.nodes:
            return

        self.nodes[node] = []

    def addEdge(self, node1, node2):
        self.nodes[node1].append(node2)

    def print(self):
        print(self.nodes)

    def cycle(self, start):
        if not start in self.nodes.keys():
            raise ValueError ("Starting point not in tree")

        stack = []
        stack.append(start)
        visited = set()


        while stack:
            current_node = stack.pop()
            
            if not current_node in visited:
                
                visited.add(current_node)

                neighbors = self.nodes[current_node]

                for neighbor in neighbors:
                    if neighbor in visited:
                        return True
                        #returns true if theres a cycle present, false otherwise
                    
                    else:
                        stack.append(neighbor)

        return False


    

def Courses(number, prereqs):
    graph = Graph()
    allowed_classes = [i for i in range(number)]

    for edge in prereqs:

        if not edge[0] in allowed_classes or not edge[1] in allowed_classes:
            raise ValueError ("Invalid class number(s) given")

        else:
            graph.addNode(edge[0])
            graph.addNode(edge[1])
            
            graph.addEdge(edge[1], edge[0])

    #since we want to return true if there's no cycle and false if there is one we have to negate our answer 
    #from the cycle detection function
    return not graph.cycle(0)



if __name__ == "__main__":
    #testing the cycle detection function
    graph1 = Graph()
    graph1.addNode(1)
    graph1.addNode(2)
    graph1.addNode(3)
    graph1.addNode(4)

#   1 -> 2
#   ↓    ↑ 
#   3    4

    graph1.addEdge(1, 2)
    graph1.addEdge(1, 3)
    graph1.addEdge(4, 2)
    assert(graph1.cycle(1) == False)

#   1 -> 2
#   ↓    ↑ 
#   3    4

    graph2 = Graph()
    graph2.addNode(1)
    graph2.addNode(2)
    graph2.addNode(3)
    graph2.addNode(4)

#   1 -> 2
#   ↑    ↓
#   3 <- 4

    graph2.addEdge(1, 2)
    graph2.addEdge(2, 4)
    graph2.addEdge(4, 3)
    graph2.addEdge(3, 1)
    assert(graph2.cycle(1) == True)

#   1 -
#   ↑  |
#    --

    graph3 = Graph()
    graph3.addNode(1)
    graph3.addEdge(1, 1)
    assert(graph3.cycle(1) == True)

#testing the numCourses function
    assert(Courses(2, [[1, 0]]) == True)
    assert(Courses(2, [[1, 0], [0, 1]]) == False)
    assert(Courses(5, [[0, 1], [1, 2], [2, 4], [4, 2], [2, 3], [3, 0]]) == False)



