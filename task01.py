'''#1. Class yaratish.Task: Car nomli class yozing. Unda brand, model, year atributlari bo'lsin va obyekt haqida ma'lumot qaytaradigan get_info() methodini yozing.'''
 
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand} Model: {self.model} Year: {self.year}"


car1 = Car("BMW", "X5", 2020)
print(car1.get_info())


