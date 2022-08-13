import random
import numpy as np
import heapq
import itertools


def createInputFile(fileName, size):
#Code used to create the random list csv file of specified size
    with open(fileName, "w") as csvfile:

        for i in range(size - 1):
            int = random.randint(1, 1000)
            csvfile.write(str(int))
            csvfile.write(",\n")

        int = random.randint(1, 1000)
        csvfile.write(str(int))



#Chunk size is the amount of numbers we want to load into memory
#total_size and the size paramter used in the create InputFile must be the same number
def createSortedFiles(InputFile, chunk_size, file_num):
    filesArray = []
    with open(InputFile, "r") as file:
        arr = []

        for i in range(file_num):

            #Read 100 numbers at a time from the 1,000,000 element list and add them to a temp arr
            for j in range(chunk_size):
                num = next(file).strip()
                num = num.replace(",", "")
                arr.append(int(num))

            arr.sort()
            sorted_list = np.array(arr)
            arr = []

            filename = "sorted_arrs" + str(i) + ".csv"

            #creates 100 files each containing a sorted list of the 100 read
            with open(filename, "w") as arr_file:
                np.savetxt(arr_file, sorted_list)
                filesArray.append(filename)

    return filesArray



#Now that we have multiple smaller sorted files we must now merge them while maintaining a sorted order
#One easy approach is to use a minheap for the merging process

#in every file only read the first line (and from there add it to a heap) then remove the heap min and add it to
#the output file, then from the file you found the previous minimum go and add the next line from there until
#all files are empty

def readSortedMin(file, heap, lineNum):
    #first read first line from a file
    with open(file, "r") as sortedFile:
                num = None
                for line in itertools.islice(sortedFile, lineNum, lineNum + 1):
                    num = line
                num = float(num)
                num = int(num)
                #must turn string into a float then int as numpy makes numbers in sorted files be in scientific notation
                heapq.heappush(heap, (num, file))


def mergeSortedFiles(OutputFile, filesList, arrSize):
    heap = []
    linePerFile = [0 for i in range(len(filesList))]

    with open(OutputFile, "w") as file:

        #readSortedMin(filesList, heap, lineNum)

        for i in range(len(filesList)):
            readSortedMin(filesList[i], heap, linePerFile[i])
            linePerFile[i] += 1


        #once we have those in a list we must heapify it to ensure the root value is the minimum
        heapq.heapify(heap)
    
        while heap:
            minimum = heapq.heappop(heap)
            minimum_val = minimum[0]
            minimum_file = minimum[1]

            #To ensure when writing to the file, we don't have a comma after the last element
            if heap:
                file.write(str(minimum_val))
                file.write(",\n")

            elif not heap:
                file.write(str(minimum_val))

            lineIndex = filesList.index(minimum_file)
            lineCount = linePerFile[lineIndex]

            if lineCount < int(arrSize // len(filesList)):
                readSortedMin(minimum_file, heap, lineCount)
                linePerFile[lineIndex] += 1





if __name__ == "__main__":
    #Algorithm works for 1 million element array, runtime takes about 115 seconds to finish
    arraySize = 1000000
    #How many elements of the array we want to load into memory
    chunkSize = 100
    #Warning if given large arraySize and small Chunk size, many files will be created on your computer of sorted lists
    fileNum = int(arraySize // chunkSize)
    #Parameters are the name you want the file to be and the size of the array in file
    createInputFile("RandomList.csv", arraySize)
    #returns a list of all sorted files
    filesList = createSortedFiles("RandomList.csv", chunkSize, fileNum)
    #returns the final sorted output in a file you name
    mergeSortedFiles("Output.csv", filesList, arraySize)



