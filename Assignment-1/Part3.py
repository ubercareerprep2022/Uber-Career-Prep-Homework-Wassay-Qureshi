class Stack:
    def __init__(self, V = None): 
        self.len = 0
        self._V = [] #V holds our list of elements in our stack
        self.minimum_list = []
        self.minimum = None

        if V is not None: #If we have a list of values we want to add into our stack then push them on individually
            for v in V:
                self.push(v)

    def push(self, item):
        #When adding a new value, if minimum is not defined then set it to item
        if self.minimum is None: 
            self.minimum = item

        #if we're pushing on an item smaller than minimum, set minimum to that item
        if item < self.minimum:
            self.minimum = item 

        self.minimum_list.append(self.minimum)
        self._V.append(item)
        self.len += 1

    def pop(self):
        #If we're trying to pop from an empty Stack, raise an IndexError
        if self.len == 0:
            raise IndexError ("Cannot pop as there are no elements in the Stack.")

        self.len -= 1
        self.minimum_list.pop()
        return self._V.pop()

    def top(self):
        #takes care of edge case where our stack is empty
        if self.len == 0:
            raise IndexError ("Cannot find top as there are no elements in the Stack.")
        #top will be the last item in our list, so return that
        return self._V[self.len - 1]

    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

    def size(self):
        return self.len

    def min(self):
        if self.len == 0:
            raise IndexError ("Cannot find minimum as there are no elements in the Stack.")
        return self.minimum_list[self.len - 1]

class Queue:
    def __init__(self, V = None):
        self._V = [] #V will preserve the order of all elements that have been enqueued and dequeued
        self.items = set() #will hold all the current items in our queue
        self.len = 0
        self.head = 0

        if V is not None: #If we have a list of values we want to add into our queue then push them on individually
            for v in V:
                self.enqueue(v)

    def enqueue(self, item):
        self._V.append(item)
        self.items.add(item)
        self.len += 1

    def dequeue(self):
        #takes care of the edge case of dequeueing from an emty queue
        if self.len == 0:
            raise IndexError ("Cannot dequeue as there are no elements in the Queue")

        item = self._V[self.head]
        self.items.remove(item)
        self.head += 1
        self.len -= 1
        return item

    def rear(self):
        return self._V[-1]

    def front(self):
        return self.head

    def size(self):
        return self.len

    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    #begin tests for Stack
    #begin test cases for the Stack Class with a list of numbers
    Stack1_vals = [3, 1, 0, 2, 3, 4, 5, 6, 7, 8]
    Stack1 = Stack(Stack1_vals)

    for i in range(len(Stack1_vals)):
        assert (Stack1.size() == len(Stack1_vals) - i)
        assert (Stack1.min() == min(Stack1._V))
        assert (Stack1.isEmpty() == False)
        assert (Stack1.top() == Stack1_vals[len(Stack1_vals) - 1 - i])
        assert (Stack1.pop() == Stack1_vals[len(Stack1_vals) - 1 - i])
    assert (Stack1.isEmpty() == True)
            
    #begin test cases for our Stack class with a list of strings
    Stack2_vals = ["b", "a", "c", "abcde", "#$%^", ""]
    Stack2 = Stack(Stack2_vals)

    for i in range(len(Stack2_vals)):
        assert (Stack2.size() == len(Stack2_vals) - i)
        assert (Stack2.min() == min(Stack2._V))
        assert (Stack2.isEmpty() == False)
        assert (Stack2.top() == Stack2_vals[len(Stack2_vals) - 1 - i])
        assert (Stack2.pop() == Stack2_vals[len(Stack2_vals) - 1 - i])
    assert (Stack2.isEmpty() == True)

    #test to make sure Stack initializes correctly even if not given an input list or inputs of different types
    Stack3 = Stack([[], [1, 2, 3, 4], [-1, 2, 5, 12]])
    assert (Stack3.min() == [])
    Stack4 = Stack([1.234, 2.3135, 6.4322])
    assert (Stack4.min() == 1.234)
    Stack5 = Stack()
    
    #tests to cover edge cases
    try:
        Stack5.pop()
    except:
        IndexError

    try:
        Stack5.top()
    except:
        IndexError

    try:
        Stack5.min()
    except:
        IndexError

    #begin tests for Queue
    #begin tests for Queue Class with a list of numbers
    Queue1_vals = [5, 4, 0, 2, 6, 7]
    Queue1 = Queue(Queue1_vals)

    for i in range(len(Queue1_vals)):
        assert (Queue1.size() == len(Queue1_vals) - i)
        assert(Queue1.front() == i)
        assert(Queue1.rear() == Queue1_vals[len(Queue1_vals) - 1])
        assert (Queue1.dequeue() == Queue1_vals[i])
    assert (Queue1.isEmpty() == True)
    Queue1.enqueue(1)
    assert (Queue1.size() == 1)
    assert (Queue1.dequeue() == 1)
    
    #begin tests for Queue Class with a list of strings
    Queue2_vals = ["ad", "%^*", "", "newcbwuc", "y2ry"]
    Queue2 = Queue(Queue2_vals)

    for i in range(len(Queue2_vals)):
        assert (Queue2.size() == len(Queue2_vals) - i)
        assert(Queue2.front() == i)
        assert(Queue2.rear() == Queue2_vals[len(Queue2_vals) - 1])
        assert (Queue2.dequeue() == Queue2_vals[i])
    assert (Queue2.isEmpty() == True)
    Queue2.enqueue("hello")
    assert (Queue2.size() == 1)
    assert (Queue2.dequeue() == "hello")

    #begin tests for Queue Class with a list of items with different types
    Queue3_vals = ["ad", 123, 1.4536, "&*"]
    Queue3 = Queue(Queue3_vals)

    for i in range(len(Queue3_vals)):
        assert (Queue3.size() == len(Queue3_vals) - i)
        assert(Queue3.front() == i)
        assert(Queue3.rear() == Queue3_vals[len(Queue3_vals) - 1])
        assert (Queue3.dequeue() == Queue3_vals[i])
    assert (Queue3.isEmpty() == True)

    #tests to cover edge cases
    Queue4 = Queue()

    try:
        Queue4.dequeue()
    except:
        IndexError


        
    

