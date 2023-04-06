def union(*args) -> set:
    union_set = set()

    for item in args:
        union_set.update(item)
    return union_set


def intersect(*args) -> set:
    intersect_set = set()

    collection_item = args[0]
    for item in collection_item:
        bool_list = []
        for coll_item in args:
            bool_list.append(item in coll_item)
        if False not in bool_list:
            intersect_set.add(item)

    return intersect_set
