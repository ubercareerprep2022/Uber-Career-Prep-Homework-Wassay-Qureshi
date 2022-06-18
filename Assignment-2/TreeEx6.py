import csv
import time
from TreeEx5 import Node, BSTPhoneBook, ListPhoneBook


def PhoneBook(Book):
    with open("data.csv", "r") as data:
        reader = csv.reader(data)

        start = time.time()
        for line in reader:
            Book.insert(line[0], int(line[1]))

        end = time.time()
        elapsed = end - start #in seconds
        insertion_time = (elapsed * 1000) #in milliseconds
        print("Insert took {:0.2f} milliseconds".format(insertion_time))


    if Book.size() != 1000000:
        raise AssertionError ("Phone Book has not correctly taken the information from the csv file")
            
    print("The size of the PhoneBook is", Book.size())


    with open("search.txt", "r") as file:
        lines = file.readlines()
        find_count = 0

        start = time.time()
        for line in lines:
            name = line.strip()
            assert(Book.find(name) != -1)
            find_count += 1

        end = time.time()
        elapsed = end - start #in seconds
        search_time = (elapsed * 1000) #in milliseconds

        print("find() was called", find_count, "times")
        print("Search took {:0.2f} milliseconds".format(search_time)) 



if __name__ == "__main__":
    BSTBook = BSTPhoneBook()
    ListBook = ListPhoneBook()

    PhoneBook(ListBook)
    print()
    PhoneBook(BSTBook)

#through testing we see it takes longer to insert the contacts into the BST but the search time is drastically lower
#In the List representation, insertion is much faster but finding is much slower due to the list being unordered
