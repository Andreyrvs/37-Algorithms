def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)
    if len(first_string) != len(second_string):
        return (first_string, second_string, False)
    return (first_string, second_string)
