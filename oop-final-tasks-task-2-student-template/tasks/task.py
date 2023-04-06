import string


class Cipher:
    alphabet = list(string.ascii_uppercase)

    def __init__(self, key_word):
        self.key_word = key_word
        self.key_word_alphabet = None
        self.set_key_word_alphabet()

    def set_key_word_alphabet(self):
        key_word_list = []
        for char in self.key_word.upper():
            if char not in key_word_list:
                key_word_list.append(char)
        temp_key_word_alphabet = []
        temp_key_word_alphabet.extend(self.alphabet)
        for let in key_word_list:
            if let in temp_key_word_alphabet:
                temp_key_word_alphabet.remove(let)
        self.key_word_alphabet = key_word_list + temp_key_word_alphabet

    def encode(self, data):
        data_list = list(data)
        return self.__do_job(data_list, self.alphabet, self.key_word_alphabet)

    def decode(self, data):
        data_list = list(data)
        return self.__do_job(data_list, self.key_word_alphabet, self.alphabet)

    def __do_job(self, data_list, start_a, end_a):
        index_list = []
        result_list = []
        for char in data_list:
            index = 0
            check_char = str(char).upper()
            if check_char not in start_a:
                result_list.append(char)
            else:
                for let in start_a:
                    if check_char == let:
                        index_list.append(index)
                        if str(char).isupper():
                            res_char = end_a[index]
                        else:
                            res_char = str(end_a[index]).lower()
                        result_list.append(res_char)
                    index += 1
        result_word = ''.join(result_list)
        return result_word