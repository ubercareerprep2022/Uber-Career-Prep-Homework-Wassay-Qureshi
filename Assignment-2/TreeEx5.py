class Node():
    def __init__(self, name, number, left = None, right = None):
        self.name = name
        self.number = number
        self.left = left
        self.right = right

        if not isinstance(name, str):
            raise ValueError ("Name must be a string")

        if not isinstance(number, int):
            raise ValueError ("Phone number must be an integer")

    def insert_helper(self, name, number):
        #instructions state we can assume all unique names
        if self.name > name:
            if self.left:
                return self.left.insert_helper(name, number)
            else:
                self.left = Node(name, number)

        elif self.name < name:
            if self.right:
                return self.right.insert_helper(name, number)
            else:
                self.right = Node(name, number)

    def find_helper(self, name):
        if self.name == name:
            return self.number

        elif self.name > name:
            if self.left:
                return self.left.find_helper(name)
            else:
                return -1

        elif self.name < name:
            if self.right:
                return self.right.find_helper(name)
            else:
                return -1



class BSTPhoneBook():
    def __init__(self, root = None):
        self.root = root
        self.len = 0

        if root:
            self.len += 1

    def size(self):
        return self.len

    def insert(self, name, number):
        if not isinstance(name, str):
            raise ValueError ("Name must be a string")

        if not isinstance(number, int):
            raise ValueError ("Phone number must be an integer")

        self.len += 1

        if self.root:
            return self.root.insert_helper(name, number)
        else:
            self.root = Node(name, number)

    def find(self, name):
        if not isinstance(name, str):
            raise ValueError ("Name must be a string")

        if self.root:
            return self.root.find_helper(name)
        else:
            return -1

#implementing this function to ensure the tree is correctly inserting
def printTree(root):
    if root:
        if root.left:
            printTree(root.left)

        print(root.name, root.number, end = " ")

        if root.right:
            printTree(root.right)


class ListPhoneBook():
    def __init__(self, name = None, number = None):
        self.contacts = []
        self.len = 0

        if name and number:
            self.insert(name, number)
        
        if name and not number:
            raise ValueError ("The name and number field must either both be filled in or both be left empty")
        
    def size(self):
        return self.len

    def insert(self, name, number):
        self.len += 1
        self.contacts.append((name, number))

    def find(self, name):
        for contact in self.contacts:
            if contact[0] == name:
                return contact[1]

        return -1

if __name__ == "__main__":
    #test cases for a BST PhoneBook
    root1 = Node("AAB", 222222222)
    Book1 = BSTPhoneBook(root1)
    assert(Book1.size() == 1)
    Book1.insert("AAA", 111111111)
    assert(Book1.size() == 2)
    Book1.insert("AAC", 333333333)
    assert(Book1.size() == 3)

#      AAB
#    /     \
#  AAA      AAC

    #printTree(Book1.root)
    assert(Book1.find("AAA") == 111111111)
    assert(Book1.find("AAB") == 222222222)
    assert(Book1.find("AAC") == 333333333)
    assert(Book1.find("ZZZ") == -1)

    try:
        Book1.insert("ZZZ", "number")
    except:
        ValueError

    try:
        Book1.insert(999999999, 999999999)
    except:
        ValueError

    try:
        person = Node("ZZZ", "number")
    except:
        ValueError

    try:
        person = Node(999999999, 999999999)
    except:
        ValueError

    #tests cases for the unsorted list phone book
    Book2 = ListPhoneBook("AAA", 111111111)
    assert(Book2.size() == 1)
    Book2.insert("AAB", 222222222)
    assert(Book2.size() == 2)
    Book2.insert("AAC", 333333333)
    assert(Book2.size() == 3)

    assert(Book2.find("AAA") == 111111111)
    assert(Book2.find("AAB") == 222222222)
    assert(Book2.find("AAC") == 333333333)
    assert(Book2.find("ZZZ") == -1)

    try:
        test = ListPhoneBook("AAA")
    except:
        ValueError


