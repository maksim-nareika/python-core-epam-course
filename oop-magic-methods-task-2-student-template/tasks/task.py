class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def fly(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def name(self):
        return self.name

    def ration(self):
        return self.ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):

    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute \'fly\'")

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"