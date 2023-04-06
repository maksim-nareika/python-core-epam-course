class Counter:
    __current_counter = 0

    def __init__(self, start=0, stop=float('inf')):
        self.start = start
        self.stop = stop
        self.__current_counter = start

    def get(self):
        return self.__current_counter

    def increment(self):
        if self.__current_counter < self.stop:
            self.__current_counter += 1
        elif self.__current_counter >= self.stop:
            print("The maximal value is reached.")