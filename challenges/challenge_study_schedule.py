def study_schedule(permanence_period, target_time):
    n = len(permanence_period)

    for index in range(0, n):
        for element in permanence_period:
            if target_time == "" and verify_tuple(element) is False:
                return None

    return None


def verify_tuple(item):
    return all((
        isinstance(item, tuple),
        len(item) == 2,
        isinstance(item[1], int),
        isinstance(item[2], int),
    ))
