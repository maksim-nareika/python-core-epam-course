class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def set_value(self, arg_value):
        self.__value = arg_value

    def get_value(self):
        return self.__value
