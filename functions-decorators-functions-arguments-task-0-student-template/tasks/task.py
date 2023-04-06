from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    nums_dict = {}

    for i in range(1,num+1):
        nums_dict[i] = i*i

    return nums_dict