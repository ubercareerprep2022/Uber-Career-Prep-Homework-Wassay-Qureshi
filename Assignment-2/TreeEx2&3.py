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
        #same structure as EX 2 as we're exploring every node of the tree but this time using a 
        #counter variable to count every time we go into a child node
        count = 0
        Employees = Queue()
        Employees.enqueue(self.root)

        while Employees.size() > 0:
            for i in range(Employees.size()):
                Employee = Employees.dequeue()

                for i in Employee.directReports:
                    Employees.enqueue(i)

            count += 1 
            
        print(count)

    
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
    Company.printNumLevels()

    #testing for case of 1 node

    CEO = Employee("A", "CEO")
    Company2 = Organization_Structure(CEO)

    Company2.printLevelByLevel()
    Company2.printNumLevels()
