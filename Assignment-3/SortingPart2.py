import random
import numpy as np

def createInputFile(fileName, size):
#Code used to create the random list csv file
    csvfile = open(fileName, "w")

    for i in range(size - 1):
        int = random.randint(1, 1000)
        csvfile.write(str(int))
        csvfile.write(",\n")

    int = random.randint(1, 1000)
    csvfile.write(str(int))

    csvfile.close()

#Chunk size is the amount of numbers we want to load into memory
#total_size and the size paramter used in the create InputFile must be the same number
def createSortedFiles(InputFile, total_size, chunk_size):
    with open(InputFile, "r") as file:
        arr = []
        files = 10

        for i in range(files):

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


    
if __name__ == "__main__":
    arraySize = 1000
    createInputFile("RandomList.csv", arraySize)
    createSortedFiles("RandomList.csv", arraySize, 100)
