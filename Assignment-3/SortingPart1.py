#When partitioning our list we want to choose a pivot in arr, which will be the last element of arr to keep it simple

def partition(arr, end, list1_end, list2_start):

    pivot = arr[end]
    #[5, 10, 5, 20, 5, 5, 10]
    #pivot = 10
    #list1_end = [0]
    #list2_start = [0]
    #end = 6

    #Continue while mid is not greater than end
    while list2_start[0] <= end:

        #If starting element is less than pivot then swap
        if arr[list2_start[0]] < pivot:
            arr[list2_start[0]], arr[list1_end[0]] = arr[list1_end[0]], arr[list2_start[0]]
            list2_start[0] += 1
            list1_end[0] += 1
             
        #If ending element is greater than pivot then swap
        elif arr[list2_start[0]] > pivot:
            arr[list2_start[0]], arr[end] = arr[end], arr[list2_start[0]]
            end -= 1
             
        elif arr[list2_start[0]] == pivot:
            list2_start[0] += 1


def partitionSort(arr, start, end):

    #Base Case of 0 and 1 element arr
    if start >= end:
        return
    
    #Second Case of 2 element arr
    if end - start == 1:
         
        #If 2 element arr is unsorted then swap both elements else it's already sorted
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            return

    #Recursive Case of 3+ element arr
    list1_end = [start]
    list2_start = [start]

    #First partition our list
    partition(arr, end, list1_end, list2_start) 
    
    #Now recursively use quicksort on our arr
    partitionSort(arr, start, list1_end[0] - 1)
    partitionSort(arr, list2_start[0], end)



#Additional Function to ensure partitionSort result is correctly sorted
def sortingTest(arr):
    if len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True



if __name__ == "__main__":
    #Begin testing of 3 Partition Sort with example in HW
    arr = [5, 10, 5, 20, 5, 5, 10]
    partitionSort(arr, 0, len(arr) - 1)
    assert(sortingTest(arr))

    #Begin testing for case of 0, 1, and 2 elements
    arr2 = []
    partitionSort(arr2, 0, len(arr2) - 1)
    assert(sortingTest(arr2))

    arr3 = [10]
    partitionSort(arr3, 0, len(arr3) - 1)
    assert(sortingTest(arr3))

    arr4 = [10, 5]
    partitionSort(arr4, 0, len(arr4) - 1)
    assert(sortingTest(arr4))

    #Additional tests to ensure algorithm works correctly
    arr5 = [1, 3, 2, 1, 1, 2, 3, 3, 2, 2, 3, 3, 2, 1, 2, 1]
    partitionSort(arr5, 0, len(arr5) - 1)
    assert(sortingTest(arr5))



