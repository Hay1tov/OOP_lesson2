class Library:
    def __init__(self, name, location, books, service ) -> None:
        self.name = name
        self.location = location
        self.books = books
        self.service = service
        
    def infos(self):
        if self.books.upper() == "ilmiy".upper():
            print(f"\nLibrary name: {self.name}\nLocation: {self.location}\nBook: {self.books}\nService: {self.service}")          
            
library1 = Library("Kitoblar Olami", "Toshkent, Yunusobod", "Sarguzasht", "Uyga yetkazib berish mavjud")
library2 = Library("Kitob Mavzusi", "Samarqand, Rudakiy", "Ilmiy", "Onlayn buyurtmalarni qabul qilish")
library3 = Library("O'qish Uyi", "Buxoro, Markaz", "Ilmiy", "Do'konda olib ketish")
library4 = Library("Bilim Dunyosi", "Andijon, Yangiobod", "Biografiya", "A'zo bo'lishda chegirmalar")
library5 = Library("Knowledge Hub", "Nukus, Qoraqalpog'iston", "Sarguzasht", "100,000 so'mdan ortiq buyurtmalarga bepul yetkazib berish")
library6 = Library("Sahifa", "Fergana, Qo'shtepa", "San'at", "Kutubxona tadbirlari va o'qishlar")


libraries = [library1, library2, library3, library4, library5, library6]

for library in libraries:
    library.infos()