from __future__ import annotations
from typing import Type


class Currency:
    currency_value = None
    currency_code = None

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        result = other_cls.currency_value/cls.currency_value
        return f"{result} {other_cls.currency_code} for 1 {cls.currency_code}"

    def __str__(self):
        return f"{self.value} {self.currency_code}"

    def to_currency(self, other_cls: Type[Currency]):
        result = self.value * other_cls.currency_value / self.currency_value
        return other_cls(result)

    def __add__(self, other):
        value = self.value + other.to_currency(self.__class__).value
        return self.__class__(value)

    def __lt__(self, other):
        return self.value < other.to_currency(self.__class__).value

    def __gt__(self, other):
        return self.value > other.to_currency(self.__class__).value

    def __eq__(self, other):
        return self.value == other.to_currency(self.__class__).value


class Euro(Currency):
    currency_value = 1.0
    currency_code = 'EUR'

    def __init__(self, value):
        super().__init__(value)


class Dollar(Currency):
    currency_value = 2.0
    currency_code = 'USD'

    def __init__(self, value):
        super().__init__(value)


class Pound(Currency):
    currency_value = 100.0
    currency_code = 'GBP'

    def __init__(self, value):
        super().__init__(value)