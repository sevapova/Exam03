'''4. Multiple Inheritance
Task: Duck classini Flyer va Swimmer dan meros oling.'''


class Falyer():
    def fly(self):
        print("Duck is flying")

class Swimmer():
    def swim(self):
        print("Duck is swimming")

class Duck(Falyer, Swimmer):
        pass


duck = Duck()
duck.fly()
duck.swim()