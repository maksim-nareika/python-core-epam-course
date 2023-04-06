from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result_dicts = []
    for dict_item in data:
        if selector(dict_item) != {}:
            temp_dict = selector(dict_item)
            bool_list = []
            for filt in filters:
                bool_list.append(filt(temp_dict))
            if False not in bool_list:
                result_dicts.append(temp_dict)

    return result_dicts


def select(*columns: str) -> ModifierFunc:
    """
    Return a function that selects only the specified fields from a dictionary.

    Args:
        *columns: The names of the fields to select.

    Returns:
        A function that takes a dictionary and returns a new dictionary with only the selected fields.
    """

    def select_fn(fr_dict: dict):
        result_dict = {}
        for field in columns:
            if fr_dict.get(field) is not None:
                result_dict[field] = fr_dict.get(field)
        return result_dict

    return select_fn


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return a function that filters a dictionary by the specified key and values.

    Args:
        column: The key to filter by.
        *values: The values to filter for.

    Returns:
        A function that takes a dictionary and returns True if the key is in the dictionary and its value is in the specified values, False otherwise.
    """

    def filter_fn(fr_dict: dict):
        marker = False

        if fr_dict.get(column) is not None:
            if fr_dict.get(column) in values:
                marker = True
        return marker

    return filter_fn


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
