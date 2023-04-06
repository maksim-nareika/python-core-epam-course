from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    zero_message = "division by zero"
    invalid_message = "invalid literal for int() with base 10: "

    num_list = str_with_ints.split()
    try:
        for num in num_list:
            if not num.isdigit():
                error_message = invalid_message + "\'" + num + "\'"
                raise NotImplementedError(f"Error code: {error_message}")
        if int(num_list[1]) == 0:
            raise NotImplementedError(f"Error code: {zero_message}")
    except NotImplementedError as e:
        return str(e)

    return float(num_list[0]) / float(num_list[1])


class NotImplementedError(Exception):
    pass