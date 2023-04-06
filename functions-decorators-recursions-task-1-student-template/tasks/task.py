from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total_sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total_sum += seq_sum(item)
        else:
            total_sum += item
    return total_sum