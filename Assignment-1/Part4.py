import random #only using random for testing purposes

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, L = None):
        self.head = None #points to first element in our LL
        self.len = 0

        #if we are given an optional input list, add each item in that list into our Linked List
        if L is not None:
            for item in L:
                self.push(item)

    def push(self, item): 
        if self.len == 0:
            self.head = Node(item, None)

        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = Node(item, None)

        self.len += 1

        
    def pop(self):
        if self.len == 0:
            raise IndexError ("Cannot pop from an empty Linked List")

        #if popping from a LL with 1 element then we're changing the head to None
        elif self.len == 1:
            item = self.head.value
            self.head = None
            self.len -= 1
            return item

        else:
            pointer = self.head

            while pointer.next.next is not None:
                pointer = pointer.next

            item = pointer.next.value 
            pointer.next = None
            self.len -= 1
            return item


    def insert(self, index, node):
        #covers various edge cases
        if index < self.len * -1:
            raise IndexError ("Error Index out or range")

        if not isinstance(index, int):
            raise ValueError ("Index must be an integer")

        if index == 0:
            pointer = self.head
            self.head = Node(node, pointer)
            self.len += 1

        elif index >= self.len * -1 and index < 0: #covers edge cases for indices like -1 and -5
            return self.insert(self.len + index, node)

        elif index <= self.len:
            pointer = self.head
            curr_index = 0

            while curr_index + 1 != index:
                pointer = pointer.next
                curr_index += 1

            temp = pointer.next
            pointer.next = Node(node, temp)
            self.len += 1

        #if index is above the size of the list do nothing according to the instructions

    def remove(self, index):
        if self.len == 0:
            return

        if not isinstance(index, int):
            raise ValueError ("Index must be an integer")

        if index == 0:
            self.head = self.head.next
            self.len -= 1

        elif index >= self.len * -1 and index < 0: #covers edge cases for small negative indices like -1 and -5
            return self.remove(self.len + index)

        elif index <= (self.len - 1):
            curr_index = 0
            pointer = self.head

            while curr_index + 1 != index:
                pointer = pointer.next
                curr_index += 1

            temp = pointer.next.next
            pointer.next = temp
            self.len -= 1

        #if index doesn't have a node, do nothing according to instructions

    def elementAt(self, index):
        if not isinstance(index, int):
            raise ValueError ("Index must be an integer")
            
        #if no node at the index or LL is empty return None
        if index > self.len or self.len == 0:
            return None

        if index >= self.len * -1 and index < 0: #covers edge cases for small negative indices like -1 and -5
            return self.elementAt(self.len + index)

        elif index == 0:
            return self.head.value

        else:
            curr_index = 0
            node = self.head

            while curr_index != index:
                node = node.next
                curr_index += 1

            return node.value

    def size(self):
        return self.len

    def printList(self):
        node = self.head
        values = []

        if self.len == 0:
            return values

        while node.next is not None:
            values.append(node.value)
            node = node.next
        values.append(node.value)

        print(values)

    def inList(self, item): #extra function I defined to make testing easier
        pointer = self.head

        while pointer is not None:
            if pointer.value == item:
                return True

            pointer = pointer.next
        
        return False

    def hasCycle(self):
        pointer = self.head
        visited = []

        while pointer is not None:
            if (pointer in visited):
                return True

            visited.append(pointer)
            pointer = pointer.next
 
        return False

    def isPalindrome(self): #Bonus Function
        if self.hasCycle() == True:
            raise ValueError ("Error LL must not have a cycle to check isPalindrome")

        values = []
        pointer = self.head

        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next

        return values == values[::-1]

if __name__ == "__main__":
    #begin tests for LL

    #begin pre-defined tests
    LL1 = LinkedList()
    LL1_vals = [random.randint(-100, 100) for i in range(random.randint(5, 25))]

    def testPushBackAddsOneNode(LL1):
        for i in range(len(LL1_vals)):
            LL1.push(LL1_vals[i])
            assert(LL1.size() == i + 1)

    def testPopBackRemovesCorrectNode(LL1):
        for i in range(len(LL1_vals)):
            assert (LL1.pop() == LL1_vals[(i + 1) * -1])
            assert(LL1.size() == len(LL1_vals) - (i + 1))

    testPushBackAddsOneNode(LL1)
    testPopBackRemovesCorrectNode(LL1)

    LL2_inputs = [1, 2, 3, 4, 5]
    LL2 = LinkedList(LL2_inputs)
    LL2_val = random.randint(-100, 100)

    def testEraseRemovesCorrectNode(LL2):
        LL2.insert(0, LL2_val)
        assert(LL2.inList(LL2_val))
        LL2.remove(0)
        assert(LL2.inList(LL2_val) == False)
            
    testEraseRemovesCorrectNode(LL2)

    LL3 = LinkedList()

    def testEraseDoesNothingIfNoNode(LL3):
        assert(LL3.size() == 0)
        for i in range(10):
            LL3.remove(i)
        assert(LL3.size() == 0)

    testEraseDoesNothingIfNoNode(LL3)

    LL4_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    LL4 = LinkedList(LL4_input)

    def testElementAtReturnNode(LL4):
        for i in range(len(LL4_input)):
            assert(LL4.elementAt(i) == i)

    testElementAtReturnNode(LL4)

    def testElementAtReturnsNoNodeIfIndexDoesNotExist(LL3):
        assert(LL3.size() == 0)
        for i in range(10):
            assert(LL3.elementAt(i) == None)
        assert(LL3.size() == 0)

    testElementAtReturnsNoNodeIfIndexDoesNotExist(LL3)

    def testSizeReturnsCorrectSize(LL3, LL4):
        assert(LL4.size() == 10)
        assert(LL3.size() == 0)
        for i in range(10):
            LL4.push(i)
            assert(LL4.size() == 10 + (i + 1))
            LL3.push(i)
            assert(LL3.size() == (i + 1))
        assert(LL4.size() == 20)
        assert(LL3.size() == 10)

    testSizeReturnsCorrectSize(LL3, LL4)

    LL5 = LinkedList()

    def cycleTesting(LL5):
        LL5.push(20)
        LL5.push(4)
        LL5.push(15)
        LL5.push(10)
        LL5.head.next.next.next.next = LL5.head
        assert(LL5.hasCycle() == True)

    cycleTesting(LL5)

    LL6 = LinkedList()

    def isPalindrome(LL6):
        LL6.push(1)
        LL6.push(2)
        LL6.push(3)
        LL6.push(2)
        LL6.push(1)
        assert(LL6.isPalindrome() == True)

    isPalindrome(LL6)

    #tests for edge cases

    LL7 = LinkedList()

    try:
        LL7.elementAt("hello")
    except:
        ValueError

    try:
        LL7.remove("hello")
    except:
        ValueError

    try:
        LL7.insert("hello")
    except:
        ValueError

    try:
        LL7.insert(-1000)
    except:
        IndexError

    try:
        LL7.pop()
    except:
        IndexError


