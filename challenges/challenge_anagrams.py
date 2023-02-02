def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)
    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    list_1 = list(first_string.lower())
    list_2 = list(second_string.lower())
    bubleSort(list_1)
    bubleSort(list_2)
    # print(bubleSort(list_1), bubleSort(list_2))
    string1 = ''.join(list_1)
    string2 = ''.join(list_2)
    result = bubleSort(list_1) == bubleSort(list_2)
    return (string1, string2, result)


def bubleSort(array):
    n = len(array)
    for ordered_elements in range(n - 1):
        for item in range(n - ordered_elements - 1):
            if array[item] > array[item + 1]:
                array[item], array[item + 1] = array[item + 1], array[item]

    return array
