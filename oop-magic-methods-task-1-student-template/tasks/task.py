from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other):
        if isinstance(other, str):
            return [f"{count} {other}" for count in self.values]