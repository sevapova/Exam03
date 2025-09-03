'''2. Constructor
Task: Student class yarating. introduce() methodi orqali talaba o‘zini tanishtirsin.

Input:

s = Student("Ali", 20, 2)
print(s.introduce())'''


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade 

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade}and course."
    

s = Student("Sevara", 20, 2)
print(s.introduce())
