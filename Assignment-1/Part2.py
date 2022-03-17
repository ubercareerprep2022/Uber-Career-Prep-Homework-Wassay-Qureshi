def isStringPermutation(s1: str, s2: str) -> bool:
    #code to catch the edge cases where s1 and s2 are not strings
    if not (isinstance(s1, str) or isinstance(s2, str)):
        raise ValueError ("Entries must be strings")

    #create 2 sets
    chars_s1 = set()
    chars_s2 = set()

    #if the length of the 2 strings is different they can't be permutations
    if len(s1) != len(s2):
        return False

    #add all characters in s1 & s2 into the sets then compare the 2
    for i in range(len(s1)):
        chars_s1.add(s1[i])
        chars_s2.add(s2[i])

    #if they all contain the same letters and same lengths (due to the if on line 10) then they must be permutations
    if chars_s1 == chars_s2:
        return True
    else:
        return False

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    #code to catch edge cases where inputArray isn't an array or targetSum isn't an int
    if not(isinstance(inputArray, list) or isinstance(targetSum, int)):
        return ValueError ("Inputs must be an array and an integer")

    #we'll store the pairs in our answers list
    answers = []
    
    for i in range(len(inputArray)):
        #code to catch edge case where inputArray doesn't contain only integers
        if not (isinstance(inputArray[i], int)):
            return ValueError ("All entries in array must be integers")
        for j in range(i + 1, len(inputArray)):
            #check if the sum of our 2 terms equal our targetSum variable, if yes then add the pairs to our answers list
            if inputArray[i] + inputArray[j] == targetSum:
                answers.append((inputArray[i], inputArray[j]))

    return answers


if __name__ == "__main__":
#tests for isStringPermutation function
#test cases to make sure the program works, also testing some edge cases 

    assert (isStringPermutation("hello", "llheo"))
    assert (isStringPermutation("good day", "day good"))
    assert (isStringPermutation("123", "213"))
    assert (isStringPermutation("_!&&#", "&&#!_"))

    assert not (isStringPermutation("hello", "goodbye"))
    assert not (isStringPermutation("", " "))
    assert not (isStringPermutation("hhhhhhiiiiiii", "hi"))
    assert not (isStringPermutation("hello", "goodbye"))
    assert not (isStringPermutation("hello", "hello "))
    
    #edge cases
    try:
        print(isStringPermutation(123, 213))
    except:
        ValueError

    assert (isStringPermutation("", ""))

#tests for pairsThatEqualSum function

    assert(pairsThatEqualSum([1, 1, 2, 0], 2) == [(1, 1), (2, 0)])
    assert(pairsThatEqualSum([2, 3, 5, 7, 100], 1) == [])
    assert(pairsThatEqualSum([1, -1, 2, -2], 0) == [(1, -1), (2, -2)])
    assert(pairsThatEqualSum([1, 2, 3, 4, 5], 700) == [])

    #edge cases
    try:
        pairsThatEqualSum(["3", 1, 2, 3], 3)
    except:
        ValueError

    try:
        pairsThatEqualSum(3, 3)
    except:
        ValueError

    try:
        pairsThatEqualSum([1, 2, 3], "3")
    except:
        ValueError
        
    assert(pairsThatEqualSum([], 700) == [])
