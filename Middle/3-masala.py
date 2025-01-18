from abc import abstractmethod, ABC

class Center(ABC):
    @abstractmethod
    def Teaching(self):
        pass
    
class ITMarkaz(Center):
    def __init__(self) -> None:
        pass
    
    def Teaching(self):
        return f"ITMarkazda siz dasturlashni o'rgana olasiz"


class TilMarkaz(Center):
    def __init__(self) -> None:
        pass
    
    def Teaching(self):
        return f"TilMarkazda siz ko'proq tillarni o'rgana olasiz"  


Programming = ITMarkaz()
print(Programming.Teaching())

language = TilMarkaz()
print(language.Teaching())