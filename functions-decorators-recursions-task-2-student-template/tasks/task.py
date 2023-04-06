from typing import Any, List
def linear_seq(sequence: List[Any]) -> List[Any]:
    res_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            res_list.extend(linear_seq(item))
        else:
            res_list.append(item)

    return res_list