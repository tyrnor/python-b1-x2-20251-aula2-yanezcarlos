from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def print(self):
        pass

class Buyer(Person):
    def __init__(self) -> None:
        pass

class Seller(Person):
    def __init__(self) -> None:
        pass