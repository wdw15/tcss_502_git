# class ShoppingCart:
#    def __init__(self, payment_method):
#        self.__pay_method = payment_method
#
#    def checkout(self, amount):
#        print(f"Paying ${amount} with {self.__pay_method.payment}")
#
# class PayPalPayment:
#     def __init__(self):
#        self.payment = 'PayPal'
#
# class CreditCardPayment:
#     def __init__(self):
#        self.payment = 'Credit Card'
#
# class BitcoinPayment:
#     def __init__(self):
#        self.payment = 'Bitcoin'
#
#
# # client side
# cart = ShoppingCart(CreditCardPayment())
# cart.checkout(50)
#
# cart = ShoppingCart(PayPalPayment())
# cart.checkout(75)
#
# cart = ShoppingCart(BitcoinPayment())
# cart.checkout(40)


from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, payment):
        print('here')
        pass

class CreditCardPayment(PaymentStrategy):
    # def __init__(self, initial_deposit):
    #     self.balance = initial_deposit

    def pay(self, amount):
        # self.balance -= amount
        print(f'Paying ${amount} with Credit Card')


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paying ${amount} with Paypal Card')

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paying ${amount} with Bitcoin Card')


class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
    def checkout(self, amount):
        self.payment_strategy.pay(amount)



# # client side
cart = ShoppingCart(CreditCardPayment())
cart.checkout(50)

cart = ShoppingCart(PayPalPayment())
cart.checkout(75)

cart = ShoppingCart(BitcoinPayment())
cart.checkout(40)