import random
microphone = [
    {
        "name": "unobtainable mic",
        "price": 2000000,
        "money": random.randint(1, 9999999),
        "happiness": random.randint(2, 100),
        "fame": 1000,
    },
    {
        "name": "broken mic",
        "price": 15,
        "money": random.randint(1, 5),
        "happiness": random.randint(1, 5),
        "fame": 10,
    },
    {
        "name": "cat mic",
        "price": 20,
        "money": random.randint(1, 10),
        "happiness": random.randint(2, 6),
        "fame": 20,
    },
    {
        "name": "blue mic",
        "price": 40,
        "money": random.randint(1, 15),
        "happiness": random.randint(5, 15),
        "fame": 50,
    },
    {
        "name": "champions mic",
        "price": 100,
        "money": random.randint(2, 20),
        "happiness": random.randint(10, 25),
        "fame": 80,
    },
    {
        "name": "Drake mic",
        "price": 500,
        "money": random.randint(100, 10000000),
        "happiness": random.randint(15, 50),
        "fame": 500,
    }
]




class Torotaneseyute:
    stat1 = 1
    stat2 = 1
    stat2 = int(stat2)
    stat1 = int(stat1)

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
                mica = input("pick a mic 1 through 5: ")
            if not mica.isnumeric():
                print("i said a number one through five retry")
                continue
            elif int(mica) < 1 or int(mica) > 5:   
                print("i said a number one through five retry")
                continue
            else:
                mica = int(mica)
                mics = input(f"you chose the {microphone[mica]["name"]} it costs {microphone[mica]["price"]} and you need at least {microphone[mica]["fame"]} fame to get it do you want it y/n ")
                if "y" in mics and self.money >= microphone[mica]["price"] and self.fame >= microphone[mica]["fame"]:
                    print(f"you just bought the {microphone[mica]["name"]} it makes you arouun ${microphone[mica]["money"]} and {microphone[mica]["happiness"]} fame per play but loses you like {microphone[mica]["happiness"]} happiness per play")
                    self.money -= microphone[mica]["price"]
                    self.mic = microphone[mica]["name"]
                    print(f"you have ${self.money} left")
                    print(self.mic)
                    self.stat1 = microphone[mica]["happiness"]
                    self.stat2 = microphone[mica]["money"]
                elif self.money < microphone[mica]["price"] and self.fame < microphone[mica]["fame"]:
                    print("gosh gigily darn, you aint got the fame or bread for it, get your bands and clout up you dissapointment")
                elif self.money < microphone[mica]["price"]:
                    print("you do NOT have the money for this, get yo bread up gng")
                elif self.fame < microphone[mica]["fame"]:
                    print("you dont have enough fame for this, get yo clout up gng \U0001F971")
                
    def sing(self):
        print("you tryna put on a performance")
        perform = input("y/n: ")
        if "y" in perform:
            self.happiness -= self.stat1
            self.money += self.stat2
            self.fame += self.stat1
            print(f"you now have ${self.money} and {self.fame} fame, but you now only have {self.happiness} happiness, go to sleep to increase it")
            x = random.randint(1,100)
            if int(self.happiness) <= 0 and x != 3 or x != 5 or x != 73 or x != 93 or x != 7:
                print("so eiher you got unlucky or negleckted your performer so he died ")
            elif int(self.happiness) <= 0 and x == 3 or x == 5 or x == 73 or x == 93 or x == 7:
                print(f"{self.name} blew its brains out, you treated it horibly, do better you human piece of trash")



Drake = Torotaneseyute("Drake", 0, 0, 1, 500, "y")
Drake.shop() 