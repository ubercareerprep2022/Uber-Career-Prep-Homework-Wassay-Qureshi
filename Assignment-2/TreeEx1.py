class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = Node(root)

#EX 1
def printTree(root):
    if root:
        print(root.value, end=" ")
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    tree = Tree(1)
    tree.root.left = Node(7)
    tree.root.right = Node(17)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(3)

    #     1
    #    /  \
    #   7    17
    #       /  \
    #      6    3
    
    printTree(tree.root)
    #successfully prints 1 7 17 6 3 

    tree = Tree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(5)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    #       1
    #     /   \
    #    2     5
    #   / \   / \
    #  3   4 6   7

    printTree(tree.root)
    #successfully prints 1 2 3 4 5 6 7 
