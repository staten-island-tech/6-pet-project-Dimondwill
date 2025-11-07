import random
microphone = [
    {
        "name": "unobtainable mic",
        "price": 2000000,
        "money": 9999999,
        "happiness": 100,
    },
    {
        "name": "broken mic",
        "price": 15,
        "money": 3,
        "happiness": 3 ,
    },
    {
        "name": "cat mic",
        "price": 20,
        "money": 7,
        "happiness": 7 ,
    },
    {
        "name": "blue mic",
        "price": 40,
        "money": 10,
        "happiness": 12,
    },
    {
        "name": "champions mic",
        "price": 100,
        "money": 75,
        "happiness": 25,
    },
    {
        "name": "Drake mic",
        "price": 500,
        "money": 67067,
        "happiness": 40,

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
            buy = input("you wanna buy a better mic y/n: ")
            if buy.lower() == "y":
                mica = int(input("pick a mic 1 through 5: "))
            
            if mica < 1 or mica > 5:
                print("i said a number one through five retry")
                self.playing = "y"
            else:  
                mics = input(f"you chose the {microphone[mica]["name"]} it costs {microphone[mica]["price"]} do you want it y/n ")
                if "y" in mics.lower() and self.money >= microphone[mica]["price"]:
                    stat1 = microphone[mica]["happiness"]
                    stat2 = microphone[mica]["money"]
                    self.money -= microphone[mica]["price"]
                    self.mic = microphone[mica]["name"]
                    print(self.mic)
    stat2=stas
    


    def sing(self):
        print("you tryna put on a performance")
        perform = input("y/n: ")
        if "y" in perform:
            print("put on a show ")
            self.happiness += stat2


Drake = Torotaneseyute("Drake", 0, 0, 1, 100, "y")
Drake.shop() 