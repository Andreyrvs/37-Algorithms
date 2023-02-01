def study_schedule(permanence_period, target_time):
    student_qty = 0
    if target_time is None:
        return None
    for element in permanence_period:
        test = verify_tuple(element)
        if not test:
            return None
        if element[0] <= target_time <= element[1]:
            student_qty += 1

    return student_qty


def verify_tuple(element):
    return all(isinstance(item, int) for item in element)
