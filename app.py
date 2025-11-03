import
microphone = [
    {
        "name": "unobtainable mic",
        "price": 2000000
    },
    {
        "name": "broken mic",
         "price": 15,
    },
    {
        "name": "cat mic",
        "price": 20,
    },
    {
        "name": "blue mic",
        "price": 40,
    },
    {
        "name": "champions mic",
        "price": 100
    },
    {
        "name": "Drake mic",
        "price": 500

    }
]




class Torotaneseyute:
    def __init__(self, name, fame, happieness, mic, money):
        self.name = name
        self.fame = int(fame)
        self.happiness = happieness
        self.mic = mic
        self.money = money

    def shop(self):
        buy = input("you wanna buy a better mic: ")
        if buy == "yes":
            input("pick a mic 1 through 5")
        

    def sing(self):
        print("you tryna put on a performance")
        perform = input("y/n: ")
        if "y" in perform:
            if 
