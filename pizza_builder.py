#  🍕 Pizza Builder — Challenge Steps
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary


class Pizza:
    def __init__(self, size, crust):
        self.size = size
        self.crust = crust
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        print("Added", topping)

    def remove_topping(self):
        print("Current toppings", self.toppings)
        remove_toppings = input("Do you want to remove any toppings? (no to exit)").lower()
        if remove_toppings in self.toppings:
            self.toppings.remove(remove_toppings)
        elif remove_toppings == "no":
            print("did not remove any toppings")
        else:
            print("No toppings matched")

    def print_details(self):
        print("Size: ", self.size)
        print("Crust type: ", self.crust)
        if self.toppings:
            print("Toppings: ", self.toppings)
        else:
            print("No toppings yet!")

new_pizza = Pizza("medium", "thin")
new_pizza.add_topping("Pepperoni")
new_pizza.add_topping("salami")
new_pizza.remove_topping()
new_pizza.print_details()