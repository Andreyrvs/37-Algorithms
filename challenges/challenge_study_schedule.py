def study_schedule(permanence_period, target_time):
    if target_time == "" and verify_tuple(permanence_period) is False:
        return None

    for item in permanence_period:
        for element in item:
            print(element)


def verify_tuple(item):
    return all((
        isinstance(item, tuple),
        len(item) == 2,
        isinstance(item[1], int),
        isinstance(item[2], int),
    ))
