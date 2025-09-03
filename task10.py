'''10. Inheritance + super()
Task: Employee classini Person dan meros oling.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)   
        self.job = job

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"


employee = Employee("Ali", 30, "Developer")
print(employee.info())
