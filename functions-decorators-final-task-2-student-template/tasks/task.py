from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    s_list = list(s)
    temp_s = s
    temp_list = list(temp_s)
    result_list = []
    count = 0
    for index in indexes:
        if len(s_list) < index-1:
            continue
        elif index >= 0:
            word_item = ''
            previous_index = 0 if index == indexes[0] else indexes[count-1]
            count += 1
            for i in range(previous_index, index):
                char_item = s_list[i]
                word_item += char_item
                temp_list.remove(char_item)
            result_list.append(word_item)
        elif index < 0:
            abs_index = abs(index)
            abs_word_item = ''
            for abs_index_item in range(0,abs_index):
                char_item = s_list[len(s_list) - (abs_index - abs_index_item)]
                abs_word_item += char_item
                temp_list.remove(char_item)
            result_list.append(abs_word_item)
    rest_str = ''.join(temp_list)
    if rest_str != '':
        result_list.append(rest_str)
    return result_list
