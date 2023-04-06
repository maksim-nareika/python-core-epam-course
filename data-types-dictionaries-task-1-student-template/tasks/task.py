from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    char_count_dict = {}

    for i in s:
        item = i.lower()
        if item in char_count_dict and char_count_dict[item]:
            char_count_dict[item] = char_count_dict.get(item) +1
        else:
            char_count_dict[item] = 1

    return char_count_dict


city = "Tashkent"
city[0] = "t"
print(city)
