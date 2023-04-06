class Sun:
    __instance = None

    @staticmethod
    def inst():
        if Sun.__instance is None:
            return Sun()
        return Sun.__instance

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            super(Sun, cls).__new__(cls)
        return cls.__instance