def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for element in permanence_period:
        if verify_tuple(element):
            return None
        if element[0] <= target_time <= element[1]:
            counter += 1

    return counter


def verify_tuple(item):
    if item is None:
        return None
    return all((
        len(item) == 2,
        isinstance(item, tuple),
        isinstance(item[1], int),
        isinstance(item[2], int)
        ))


    # if (item is None
    #         len(item) == 2,
    #         or isinstance(item, tuple)
    #         or isinstance(item[1], int)
    #         or isinstance(item[2], int)):
    #     return None