def is_palindrome_recursive(word, low_index, high_index):
    print('high_index: ', high_index)
    print('low_index: ', low_index)
    print('word: ', word)
    if word == "":
        return False

    word = word.lower()
    if high_index < 2:
        return True
    elif range(word[low_index]) == range(word[high_index - 1]):
        return is_palindrome_recursive(
            word[1: high_index - 1], low_index, high_index
            )
    else:
        return False
