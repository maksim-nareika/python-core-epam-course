from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    result_list = []
    if len(lst) <= 1:
        return result_list
    else:
        for i in range(0,len(lst)):
            if i + 1 < len(lst):
                result_list.append((lst[i], lst[i+1]))
    return result_list
