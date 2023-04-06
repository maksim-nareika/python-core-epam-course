from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    values_set = set()

    for item in lst:
        values_set.update(set(item.values()))

    return values_set