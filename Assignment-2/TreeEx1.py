class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

class Tree:
    def __init__(self, root):
        self.root = root

#EX 1
def printTree(root):
    if root:
        print(root.value, end=" ")
        if root.children:
            for each in root.children:
                printTree(each)



if __name__ == "__main__":
    #test case for a binary tree
    node3 = Node(3)
    node6 = Node(6)
    node17 = Node(17, [node6, node3])
    node7 = Node(7)
    node1 = Node(1, [node7, node17])
    tree = Tree(node1)

    #     1
    #    /  \
    #   7    17
    #       /  \
    #      6    3
    
    printTree(tree.root)
    #successfully prints 1 7 17 6 3 
    print("")

    #test case for a non-binary tree
    node10 = Node(10)
    node9 = Node(9)
    node8 = Node(8)
    node7 = Node(7)
    node6 = Node(6)
    node5 = Node(5)
    node3 = Node(3)
    node2 = Node(2, [node5, node6, node7])
    node4 = Node(4, [node8, node9, node10])
    node1 = Node(1, [node2, node3, node4])
    tree2 = Tree(node1)

    #           1
    #         / | \
    #       /   |   \
    #      2    3    4
    #    / | \     / | \
    #   /  |  \   /  |  \
    #  5   6   7  8  9   10

    printTree(tree2.root)
    #successfully prints 1 2 5 6 7 3 4 8 9 10 
    print("")

    #test case for a tree of 1 node
    node1 = Node(1)
    tree3 = Tree(node1)

    # 1

    printTree(tree3.root)
    #successfully ptins 1 

