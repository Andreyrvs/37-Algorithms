def study_schedule(permanence_period, target_time):
    counter = 0
    for element in permanence_period:
        if target_time is None or verify_tuple(element):
            return None
        if element[0] <= target_time <= element[1]:
            counter += 1

    return counter


def verify_tuple(item):
    if (item is None
            or len(item) == 2
            or isinstance(item, tuple)
            or isinstance(item[1], int)
            or isinstance(item[2], int)):
        return None
