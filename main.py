class Wallet:
    # money = 0 -> the default value for money is 0
    def __init__(self, money=0):
        self.money = money

    def __str__(self):
        return f"This wallet has {self.money}"

    def credit(self, amount):
        # self.money = self.money + amount
        self.money += amount
        print(f"Credit: The new amount if money is {self.money}")

    def debit(self, amount):
        self.money -= amount
        print(f"Debit: The new amount if money is {self.money}")


wallet = Wallet(6)
wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet)
wallet.credit(5)
print(wallet)
wallet.debit(2)
print(wallet)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

    def __str__(self):
        return f"This person is {self.name}, they're at location {self.location} and they have {self.wallet.money} money"

    def move_to(self, point):
        self.location = point
        print(f"The new location for {self.name} is {self.location}")


person = Person("Moh", 5, 50)
person.move_to(10)


# person = {
#     name: "Shereen",
#     location: 5,
#     wallet: {
#         money: 4,
#         credit: fn,
#         debit: fn
#     }
# }


class Vendor(Person):
    range = 5
    price = 1

    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def sell_to(self, customer, number_of_icecreams):
        cost = number_of_icecreams * self.price
        self.move_to(customer.location)
        customer.wallet.debit(cost)
        self.wallet.credit(cost)
        print(f"{number_of_icecreams} Icecreams are sold")

    # Moves to the customer's location
    # Transfers money from the customer's wallet to the vendor's wallet
    #  Prints a nice message saying how many icecreams were sold


class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def _is_in_range(self, vendor):
        distance = abs(self.location - vendor.location)
        if distance <= vendor.range:
            print(f"This vendor {vendor.name} is within {self.name} range")
            return True
        else:
            print(f"This vendor {vendor.name} is NOT within {self.name} range")
            return False

    def _have_enough_money(self, vendor, number_of_icecreams):
        cost = vendor.price * number_of_icecreams
        if self.wallet.money >= cost:
            return True
        else:
            return False

    def request_icecream(self, vendor, number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(
            vendor, number_of_icecreams
        ):
            vendor.sell_to(self, number_of_icecreams)
            print("YAY LET'S EAT ICECREAM")


vendor_one = Vendor("Talal", 3, 60)
vendor_two = Vendor("Lateefa", 81, 500)
customer_one = Customer("Abbas", 80, 6)

customer_one.request_icecream(vendor_two, 5)
