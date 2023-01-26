def study_schedule(permanence_period, target_time):

    n = len(permanence_period)

    for index in range(0, n):
        for element in permanence_period:
            if target_time == "" and verify_tuple(element) is False:
                return None

            print('element: ', element)

            if permanence_period[index] == target_time:
                print('2: ', index)
                return index

    return None


def verify_tuple(item):
    return all((
        isinstance(item, tuple),
        len(item) == 2,
        isinstance(item[1], int),
        isinstance(item[2], int),
    ))


    # if target_time == "" and verify_tuple(permanence_period) is False:
    #     return None

    # count_student = 0
    # for item in permanence_period:
    #     print('item: ', item)
    #     for element in item:
    #         if item[element] == target_time:
    #             count_student += 1
    #             print('element: ', element)

    # return count_student