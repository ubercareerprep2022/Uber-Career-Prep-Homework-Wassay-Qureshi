#Merge arr1 and arr2 using O(1) asymptotic space
def Merge(arr1, arr2):

    #We know the larger of the 2 arrays will be the one that holds the buffer
    if len(arr1) > len(arr2):
        buffer_arr = arr1
        smaller_arr = arr2

    else:
        buffer_arr = arr2
        smaller_arr = arr1

    buff_size = 0
    #buff_size is the amount of numbers in the buffer list
    for i in range(len(buffer_arr)):
        if buffer_arr[i] != None:
            buff_size += 1

    #smaller_size is the size of the smaller non-buffer list
    smaller_size = len(smaller_arr)

    #Raise ValueError if there is not enough space in the list to hold the smaller arr in the buffer arr
    if smaller_size > len(buffer_arr) - buff_size:
        raise ValueError ("Error list doesn't hold large enough buffer")

    i = buff_size - 1  #i is the max index of buff arr that still returns a number
    j = smaller_size - 1 #j is the max index of smaller arr

    # Move p backwards through the array, each time finding
    # the smallest value at i or j.
    for x in range(len(buffer_arr) - 1, -1, -1):

        if i >= 0 and buffer_arr[i] > smaller_arr[j]:
            buffer_arr[x] = buffer_arr[i]
            i -= 1

        else:
            buffer_arr[x] = smaller_arr[j]
            j -= 1

    return buffer_arr


#Additional Function to ensure Merge result is correctly sorted
def sortingTest(arr):
    if len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True



if __name__ == '__main__':
    #begin testing for Merge function
    arr1 = [2, 4, 6, 8, 10, None, None, None, None, None]
    arr2 = [1, 3, 5, 7, 9]
    
    assert(sortingTest(Merge(arr1, arr2)))

    arr3 = [-2, 10, 15]
    arr4 = [-1, 0, 5, 7, 19, None, None, None]

    assert(sortingTest(Merge(arr3, arr4)))

    arr5 = [1, 3, 5, 7, 9, None]
    arr6 = [2, 4, 6, 8, 10]

    try:
        Merge(arr5, arr6)
    except:
        ValueError

