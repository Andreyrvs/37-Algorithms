def is_palindrome_recursive(word, low_index, high_index):
    n = len(word)
    if n == 0:
        return True

    return is_palc_rec(word, low_index, high_index - 1)


def is_palc_rec(word, low_index, high_index):
    if low_index == high_index:
        return True

    if (word[low_index] != word[high_index]):
        return False
    if low_index < high_index + 1:
        return is_palc_rec(word, low_index + 1, high_index + 1)
    return True
