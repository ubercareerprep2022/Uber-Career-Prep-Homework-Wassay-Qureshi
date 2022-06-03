from Part3 import Queue
#importing previously built Queue data structure from HW 1 part 3

class Employee:
    def __init__(self, name, title, directReports = []):
        self.name = name
        self.title = title
        self.directReports = directReports

class Organization_Structure:
    def __init__(self, root):
        self.root = root

    #EX 2
    def printLevelByLevel(self):
        Employees = Queue()
        Employees.enqueue(self.root)

        while Employees.size() > 0:
            for i in range(Employees.size()):
                Employee = Employees.dequeue()
                print("Name: ", Employee.name, end = ", ")
                print("Title: ", Employee.title)

                for i in Employee.directReports:
                    Employees.enqueue(i)

            print("")

    #EX 3
    def printNumLevels(self):
        max_level = 0

    
if __name__ == "__main__":
    #setting up the organization structure
    Sales_Intern = Employee("K", "Sales Intern")
    Sales_Rep = Employee("J", "Sales Representative", [Sales_Intern])
    Director = Employee("I", "Director", [Sales_Rep])
    CFO = Employee("B", "CFO", [Director])
    Engineer_F = Employee("F", "Engineer")
    Engineer_G = Employee("G", "Engineer")
    Engineer_H = Employee("H", "Engineer")
    Manager_D = Employee("D", "Manager", [Engineer_F, Engineer_G, Engineer_H])
    Manager_E = Employee("E", "Manager")
    CTO = Employee("C", "CTO", [Manager_D, Manager_E])
    CEO = Employee("A", "CEO", [CFO, CTO])
    Company = Organization_Structure(CEO)

    #Test for Ex 2 
    Company.printLevelByLevel()

