class Torotaneseyute:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, price, item):
        if self.money > price:
            self.inventory.append(item)
            self.money -= price
            print(f"Wagwan crodie, you just lost ${price} but you still got {self.money} left Croodie")
        elif self.money < price:
            print("Ayo top left Croskie gotta get yo bands up fo you get slimed out on Sankofa square fam")
        elif self.money == price:
            self.inventory.append(item)
            self.money -= price
            print(f"Wagwan Croski you had ")


Drake = Torotaneseyute("Drake", 100, [])
Drake.buy(50, "microphone")
Drake.buy(50, "microphone")