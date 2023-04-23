#Demo 07-02
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee =%d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

#Creating instance objects
employee1 = Employee("Phanwadee", 75000)
employee2 = Employee("Sunisa", 85000)

employee1.displayEmployee()
employee2.displayEmployee()

employee1.displayCount()
