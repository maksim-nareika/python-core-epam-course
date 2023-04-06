from abc import ABC, abstractproperty, abstractmethod
# from abc import abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        raise NotImplementedError("You have to implement wheels_num() method")

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {type(self).__name__}"

    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2

    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage
        result_price = price if price >= 1_00_000 else 1_00_000
        return result_price


# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6