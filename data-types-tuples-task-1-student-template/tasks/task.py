from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    num_list = []
    str_mums = str(num)
    for i in str_mums:
        num_list.append(int(i))

    return tuple(num_list)