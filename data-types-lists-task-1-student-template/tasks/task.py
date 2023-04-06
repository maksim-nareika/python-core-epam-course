from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    uniq_words = sorted(set(str_list))
    return list(uniq_words)