from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    result_dict = {}

    for dict_item in args:
        for key in dict_item.keys():
            if key not in result_dict:
                result_dict[key] = dict_item.get(key)
            else:
                result_dict[key] = result_dict.get(key) + dict_item.get(key)

    return result_dict