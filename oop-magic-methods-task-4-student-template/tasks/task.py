class PriceControl:
    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NameControl:
    def __set__(self, instance, value):
        if instance.__dict__.get(self.name) is not None:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
