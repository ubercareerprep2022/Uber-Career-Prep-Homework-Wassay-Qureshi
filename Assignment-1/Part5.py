from Part4 import Node, LinkedList
from Part3 import Stack
#importing these files to use the previously defined Data Structures from parts 3 and 4
import random
#importing random only for testing

def reverseLinkedListIter(L):
    #function takes a LL and reverses it iteratively
    current_node = L.head
    previous_node = None
    following_node = None
    while current_node is not None:
        following_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = following_node
    L.head = previous_node

    return L
  
def reverseLinkedListStack(L):
    #function takes a LL and reverses it using a stack
    stack = Stack() 
    pointer = L.head
    while pointer is not None:
        stack.push(pointer.value)
        pointer = pointer.next

    L.empty() #new function I defined in the part 4 file to empty our LL
    while stack.len > 0:
        L.push(stack.pop())

    return L

def reverseLinkedListRecurHelper(L, pointer): #Using a helper function to make calling the function on the user end easier
    if (pointer == None): 
        return pointer
          
    if (pointer.next == None): 
        return pointer
          
    reversed_list = reverseLinkedListRecurHelper(L, pointer.next) #recursive call to next node
    pointer.next.next = pointer
    pointer.next = None
    return reversed_list

def reverseLinkedListRecur(L):
    #function takes a LL and reverses it recursively using a helper
    L.head = reverseLinkedListRecurHelper(L, L.head)

    return L

if __name__ == "__main__":
    #testing with a predefined list
    LL1234_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    LL1 = LinkedList(LL1234_vals)
    LL2 = LinkedList(LL1234_vals)
    LL3 = LinkedList(LL1234_vals)
    LL4 = LinkedList(LL1234_vals)

    reverseLinkedListIter(LL2)
    reverseLinkedListStack(LL3)
    reverseLinkedListRecur(LL4)

    assert(LL1.isReversed(LL2)) #isReversed is a new function I built into the part 4 HW code
    assert(LL1.isReversed(LL3))
    assert(LL1.isReversed(LL4))
    assert(LL2.getList() == LL3.getList() == LL4.getList()) #ensures all 3 reverse functions correctly reverse the list, built getList function into HW 4 code

    #testing with a random list
    LL5678_vals = [random.randint(-100, 100) for i in range(random.randint(5, 25))]
   
    LL5 = LinkedList(LL5678_vals)
    LL6 = LinkedList(LL5678_vals)
    LL7 = LinkedList(LL5678_vals)
    LL8 = LinkedList(LL5678_vals)

    reverseLinkedListIter(LL6)
    reverseLinkedListStack(LL7)
    reverseLinkedListRecur(LL8)
    
    assert(LL5.isReversed(LL6))
    assert(LL5.isReversed(LL7))
    assert(LL5.isReversed(LL8))
    assert(LL6.getList() == LL7.getList() == LL8.getList())    
   
    #edge case for an empty LL
    LL9 = LinkedList()
    LL10 = LinkedList()
    LL11 = LinkedList()
    LL12 = LinkedList()

    reverseLinkedListIter(LL10)
    reverseLinkedListStack(LL11)
    reverseLinkedListRecur(LL12)
    
    assert(LL9.isReversed(LL10))
    assert(LL9.isReversed(LL11))
    assert(LL9.isReversed(LL12))
    assert(LL10.getList() == LL11.getList() == LL12.getList())

