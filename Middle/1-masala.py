class Car:
    def __init__(self, name=None, color=None, price=None, marka=None, year=None) ->None:
        self.name = name
        self.color =color
        self.price = price
        self.age = marka
        self.year = year
        
    def getter(self):
        self.name = input("\nMashina turini kiriting: ")
        self.color = input("Mashina rangini kiriting: ")
        self.marka = input("Mashina markasini kiriting: ")
        self.price = int(input("Mashinaning narxini kiriting: "))
        self.year = input("Nechanchi yil chiqqan: ")
        
    def setter(self):
        print(f"\nModel: {self.name}\nYear: {self.year}\nPrice: {self.price}\nColor: {self.color}\nMarka: {self.marka}")
                    
    def price_change(self, price):
        count1 = 0
        for car in cars:
            if car.name.upper() == price.upper():
                new_price = input(f"yangi narxni kiriting: ")
                if int(new_price) > 0:
                    car.price = new_price 
                    print("\nNarx o'zgartirildi")
                    count1+= 1
        if count1 == 0:
            print(f"\nBunday mashina topilmadi")
    
    def color_change(self, color):
        count2 = 0
        for car in cars:
            if car.name.upper() == color.upper():
                new_color = input(f"Mashina uchun yangi rangni yozing: ")
                car.color = new_color
                print("\nRang o'zgartirildi")
                count2+= 1
        if count2 == 0:
            print(f"\nBunday mashina topilmadi")
    
cars = []
        
n = 0  
while True:
    print(f"\nYangi mashina qo'shish - 1\nBarcha mashinalarni ma'lumotini chiqarish - 2\nMashina rangini o'zgartirish - 3\nMashina narxini o'zgartirish - 4\nDasturni yopish - 5")
    
    n = int(input("Buyruqni tanlang: "))
    
    car = Car()
    if n == 1:
        car.getter()
        cars.append(car) 
        
    if n == 2:
        for car in cars:
            car.setter()

    if n == 3:
        c = input("Mashina nomini kiriting: ")
        color = Car()
        color.color_change(c)
    
    if n == 4:
        c = input("Mashina nomini kiriting: ")
        price = Car()
        price.price_change(c)

    if n == 5:
        break
    
    if n <= 0 or n > 5:
        print(f"Bunday buyruq mavjuda emas")