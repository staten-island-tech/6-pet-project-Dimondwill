import random
microphone = [
    {
        "name": "unobtainable mic",
        "price": 2000000,
        "money": random.randint(1, 9999999),
        "happiness": random.randint(2, 100) ,
    },
    {
        "name": "broken mic",
        "price": 15,
        "money": random.randint(1, 5),
        "happiness": random.randint(1, 5) ,
    },
    {
        "name": "cat mic",
        "price": 20,
        "money": random.randint(1, 10),
        "happieness": random.randint(2, 6) ,
    },
    {
        "name": "blue mic",
        "price": 40,
        "money": random.randint(1, 15),
        "happiness": random.randint(5, 15),
    },
    {
        "name": "champions mic",
        "price": 100,
        "money": random.randint(2, 20),
        "happiness": random.randint(10, 25),
    },
    {
        "name": "Drake mic",
        "price": 500,
        "money": random.randint(100, 10000000),
        "happiness": random.randint(15, 50),
    }
]




class Torotaneseyute:
    def __init__(self, name, fame, happieness, mic, money, playing):
        self.name = name
        self.fame = int(fame)
        self.happiness = happieness
        self.mic = mic
        self.money = money
        self.playing = playing
    def shop(self):
        while self.playing == "y":
            buy = input("you wanna buy a better mic: ")
            if buy == "yes":
                mica = int(input("pick a mic 1 through 5: "))
            if mica < 1 or mica > 5:
                print("i said a number one through five retry")
                return     
            else:  
                mics = input(f"you chose the {microphone[mica]["name"]} it costs {microphone[mica]["price"]} do you want it y/n ")
                if "y" in mics and self.money >= microphone[mica]["price"]:
                    stat1 = microphone[mica]["happiness"]
                    stat2 = microphone[mica]["money"]
                    self.money -= microphone[mica]["price"]
                    self.mic = microphone[mica]["name"]
                    return(self.mic)
    


    def sing(self):
        print("you tryna put on a performance")
        perform = input("y/n: ")
        if "y" in perform:
            self.happiness


Drake = Torotaneseyute("Drake", 0, 0, 1, 100, "y")
Drake.shop() 