class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def insert_helper(self, number):
        if self.value >= number:
            if self.left:
                return self.left.insert_helper(number)
            else:
                self.left = Node(number)

        elif self.value < number:
            if self.right:
                return self.right.insert_helper(number)
            else:
                self.right = Node(number)

    def find_helper(self, number):
        if self.value == number:
            return True

        elif self.value > number:
            if self.left:
                return self.left.find_helper(number)
            else:
                return False

        elif self.value < number:
            if self.right:
                return self.right.find_helper(number)
            else:
                return False


class BST():
    def __init__(self, root = None):
        self.root = root
        self.len = 0

        if root:
            self.len += 1

    def insert(self, number):
        if not isinstance(number, int):
            raise ValueError ("Error must only insert integers into the BST")
        
        self.len += 1

        if self.root:
            return self.root.insert_helper(number)
        else:
            self.root = Node(number)
        


    def find(self, number):
        if not isinstance(number, int):
            raise ValueError ("Only integers are in the BST")

        if self.root:
            return self.root.find_helper(number)
        else:
            #The number will never be there in an empty tree
            return False



#implementing this function to ensure the tree is correctly inserting
def printTree(root):
    if root:
        if root.left:
            printTree(root.left)

        print(root.value, end = " ")

        if root.right:
            printTree(root.right)

if __name__ == "__main__":
    #begin testing for simple BST tree
    root1 = Node(2)
    BST1 = BST(root1)
    BST1.insert(1)
    BST1.insert(3)

#      2
#     / \
#    1   3

    printTree(BST1.root)
    print()
    for i in range(1, BST1.len + 1):
        assert(BST1.find(i))

    #begin testing for more complex tree
    root2 = Node(4)
    BST2 = BST(root2)
    BST2.insert(2)
    BST2.insert(6)
    BST2.insert(5)
    BST2.insert(7)
    BST2.insert(3)
    BST2.insert(1)

#            4
#          /   \
#         2     6
#        / \   / \
#       1   3 5   7

    printTree(BST2.root)
    print()
    for i in range(1, BST2.len + 1):
        assert(BST2.find(i))

#begin testing for edge cases
    try:
        BST2.insert("hello")
    except:
        ValueError

    try:
        BST2.find("hello")
    except:
        ValueError

#begin testing on an empty tree
    BST3 = BST()
    assert(BST3.find(1) == False)
    BST3.insert(1)
    assert(BST3.find(1))
