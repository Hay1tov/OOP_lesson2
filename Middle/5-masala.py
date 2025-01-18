class Book:
    def __init__(self, name=None, page=None, price=None) -> None:
        self.name = name
        self.page = page
        self.price = price
        
    def enter(self):
        self.name = input("book name: ")
        self.page = input("page: ")
        self.price = input("price: ")
        
    def increase(self):
        s = self.page + 10
        return s
    
    def decrease_price(self):
        if self.page >= 100:
            self.price /= 2
            
    
book1 = Book("Ko'zgu", 95, 300)
book2 = Book("Falsafa Asoslari", 120, 400)
book3 = Book("Tarixni O'rganish", 85, 250)
book4 = Book("Badiiy Adabiyot", 75, 200)
book5 = Book("Psixologiya va Jamiyat", 110, 350)

books = [book1, book2, book3, book4, book5]

for book in books:
    book.increase()
    book.decrease_price()
    
for book in books:
    print(f"\nName: {book.name}\nPage: {book.page}\nPrice: {book.price}")