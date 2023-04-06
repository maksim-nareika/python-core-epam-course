class HistoryDict:
    __key_list = []

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def set_value(self, key, value):
        if len(self._data.keys()) < 5:
            if self._data[key] != value:
                self.__key_list.append(key)
                self._data[key] = value
        else:
            if self._data[key] != value:
                self.__key_list.remove(self.__key_list[0])
                self.__key_list.append(key)
                self._data[key] = value

    def get_history(self):
        return self.__key_list
