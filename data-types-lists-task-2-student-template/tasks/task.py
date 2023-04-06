from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    result_list = []
    max_range = n + 1

    for i in range(1,max_range):
        if not i % 15:
            result_list.append("FizzBuzz")
        elif not i % 5:
            result_list.append("Buzz")
        elif not i % 3:
            result_list.append("Fizz")
        else:
            result_list.append(i)
    return result_list
