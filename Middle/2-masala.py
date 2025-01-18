from abc import abstractmethod, ABC

class Animal(ABC):
    def __init__(self, type, height) -> None:
        self.type = type
        self.height = height
        
    @abstractmethod 
    def Sound(self):
        pass
    
class Dog(Animal):
    def __init__(self, type, height) -> None:
        super().__init__(type, height)
        
    def Sound(self):
        return f"WOW WOW"
    
class Cat(Animal):
    def __init__(self, type, height) -> None:
        super().__init__(type, height)
        
    def Sound(self):
        return f"MEOW MEOW"
    

dog  = Dog(type="Dog", height = 10)
print(dog.Sound())

cat = Cat(type="Cat", height = 5)
print(cat.Sound())