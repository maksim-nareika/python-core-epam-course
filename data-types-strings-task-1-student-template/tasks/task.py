def get_fractions(a_b: str, c_b: str) -> str:
    result = None
    first_nums = a_b.split("/")
    second_nums = c_b.split("/")

    first_top = int(first_nums[0])
    first_bot = int(first_nums[1])
    second_top = int(second_nums[0])
    second_bot = int(second_nums[1])

    if first_bot == second_bot:
        result = f"{a_b} + {c_b} = {first_top + second_top}/{first_bot}"
    else:
        result = f"{a_b} + {c_b} = {first_top * second_bot + second_top*first_bot}/{first_bot * second_bot}"


    return result