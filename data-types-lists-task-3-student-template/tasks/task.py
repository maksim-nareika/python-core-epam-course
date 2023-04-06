from typing import List


def foo(nums: List[int]) -> List[int]:
    result_list = []

    for i in range(0,len(nums)):
        work_list = []
        work_list.extend(nums)
        work_list.pop(i)
        element_to_add = 1

        for j in range(0,len(work_list)):
            element_to_add *= work_list[j]

        result_list.append(element_to_add)

    return result_list
