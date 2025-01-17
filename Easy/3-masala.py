from os import system
from colorama import Fore, Style

system('clear')
class Animals:
    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def __str__(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} Yoshi: {Fore.YELLOW}{self.age}")

class predator(Animals):
    def __init__(self, type, age, food):
        super().__init__(type, age)
        self.food = food

    def voice(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}ovoz chiqardi!")

    def eat(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}{self.food} yedi")

class Herbivor(Animals):
    def __init__(self, type, age, ozuqa):
        super().__init__(type, age)
        self.ozuqa = ozuqa

    def voice(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}ovoz chiqardi")

    def eat(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}{self.ozuqa} yedi")

animar_prd = predator("Sher", 5, "Go'sht")
print(animar_prd)
print(animar_prd.voice())
print(animar_prd.eat())

animal_hrb = Herbivor("Qo'y", 2, "o't")
print(animal_hrb)
print(animal_hrb.voice())
print(animal_hrb.eat())
