def study_schedule(permanence_period, target_time):
    student_qty = 0
    if target_time is None or target_time == "":
        return None
    for element in permanence_period:
        verify_tuple(element)
        if element[0] <= target_time <= element[1]:
            student_qty += 1

    return student_qty


def verify_tuple(item):
    if (item is None
            or len(item) != 2
            or type(item) != tuple):
        return None
    for invalid in item:
        if invalid != int:
            return None
    return item
