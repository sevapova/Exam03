'''13. Interface-like Design
Task: Payment abstract classida pay() methodini implement qiling.
'''

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


payPalPayment1 = PayPalPayment()
payPalPayment2 = CardPayment()

payPalPayment1.pay(100)
payPalPayment2.pay(200)
