def is_anagram(first_string, second_string):
    print('first_string: ', first_string)
    print('second_string: ', second_string)
    if first_string == "" or second_string == "":
        return False
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    return True
