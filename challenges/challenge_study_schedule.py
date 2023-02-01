def study_schedule(permanence_period, target_time):
    student_qty = 0
    if target_time is None:
        return None
    for element in permanence_period:
        if verify_tuple(element):
            return None
        if element[0] <= target_time <= element[1]:
            student_qty += 1
    print('student_qty: ', student_qty)

    return student_qty


def verify_tuple(item):
    print('item: ', item)
    if item is None:
        return None
    if (len(item) != 2
            or type(item) != tuple
            or item[1] != int
            or item[2] != int):
        return None
