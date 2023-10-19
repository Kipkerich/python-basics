from abc import ABC


class Gari(ABC):
    def mileage(self):
        pass


class Toyota(Gari):
    def mileage(self):
        print("My mileage is 30kmph")


class Nissan(Gari):
    def mileage(self):
        print("My mileage is 40kmph")
