from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    result_list = []

    for i in range(row_start, row_end+1):
        temp_list = []
        for j in range(column_start, column_end+1):
            temp_list.append(i*j)

        result_list.append(temp_list)

    return result_list
