from typing import List

def split(data: str, sep=None, maxsplit=-1):

    if sep == "":
        raise ValueError("empty separator")

    sep_list = ["\n", "\r", "\t", "\f", " "]
    end_sep = []

    if sep is not None:
        end_sep.append(sep)
    else:
        end_sep.extend(sep_list)

    result_list = []

    if maxsplit == 0:
        result_list.append(data.strip())
    elif maxsplit < 0:
        word_item = ''
        for i in data.strip():
            if i not in end_sep:
                word_item += i
            elif i in end_sep:
                result_list.append(word_item)
                word_item = ''
        result_list.append(word_item)
    else:
        word_item = ''
        count = 0
        for i in data.strip():
            if count <= maxsplit-1:
                if i not in end_sep:
                    word_item += i
                elif i in end_sep:
                    count +=1
                    result_list.append(word_item)
                    word_item = ''
            else:
                word_item += i
        result_list.append(word_item)

    if result_list and result_list[0] == '' and sep_list == end_sep:
        result_list.remove('')

    return result_list