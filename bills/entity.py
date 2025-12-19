from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, dni: str, email: str, mobile: str, address: str) -> None:
        self.dni = dni
        self.email = email
        self.mobile = mobile
        self.address = address

    @abstractmethod
    def print(self) -> None:
        pass


class Buyer(Person):
    def __init__(
        self, dni: str, full_name: str, age: int, email: str, mobile: str, address: str
    ) -> None:
        super().__init__(dni, email, mobile, address)
        self.full_name = full_name
        self.age = age


class Seller(Person):
    def __init__(self, dni, email, mobile, bussines_name, bussines_addres) -> None:
        super().__init__(dni, email, mobile, bussines_addres)
        self.bussines_name = bussines_name
