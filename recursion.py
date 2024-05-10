from sys import getrecursionlimit
from sys import setrecursionlimit

setrecursionlimit(2000)
#print(getrecursionlimit())

class employee:
    """defining the employee class
    """
    def __init__(self, name, salary, subordinates=None):
        """initializing an employee with name salary and an optional list of subordinates
        """
        self.name = name
        self.salary = salary
        self.subordinates = subordinates or []

    def total_salary(self):
        """calculating the total salary of the employee and their subordinates recursively
        this method is called recursively to calculate the total salary of each employee
        the total salary of an employee is the salary of the employee plus the total salary of all their subordinates
        
        if the employee has no subordinates, their total salary is their salary
        if not self.subordinates:
            return self.salary
        
        if the employee has subordinates, their total salary is their salary plus the total salary of all their subordinates
        the total salary of a subordinate is the salary of the subordinate plus the total salary of all their subordinates"""
        total = self.salary #starting with the salary of the employee
        if not self.subordinates:
            return self.salary
        for subordinate in self.subordinates:
            #for each subordinate we are calculating their total salary recursively
            total += subordinate.total_salary()
        return total
    
    def display_organisation(self, level=0):
        #displaying the organization hierarchy
        indentation = "  " * level
        print(f"{indentation}{self.name} - Salary: ${self.salary:,.2f}")  # Include salary information
        for subordinate in self.subordinates:
            subordinate.display_organisation(level + 1)
    
#creating an organization tree
ceo = employee("John Doe", 500000)
cto = employee("Jane Doe", 400000)
hr_director = employee("Bob Smith", 300000)
data_head = employee("Michelle Muthoni", 300000)
data_engineer = employee("Joy Doe", 150000)
data_analyst = employee("James Doe", 150000)
secretary = employee("Mary Doe", 100000)

#setting up the organization hierarchy
ceo.subordinates = [cto, hr_director]
cto.subordinates = [data_head]
data_head.subordinates = [data_engineer, data_analyst]
hr_director.subordinates = [secretary]

#calculating the total salary of the organization
organisation_salary = data_head.total_salary()
print(f'Total salary remitted is: ${organisation_salary:,.2f}')

#displaying the organization hierarchy and individual salaries
data_head.display_organisation()



