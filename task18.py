'''18. Operator Overloading
Task: Time classida __lt__ metodini yozing.'''


class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour


t1 = Time(10, 30)
t2 = Time(12, 15)

print(t1 < t2)   
print(t2 < t1)   
