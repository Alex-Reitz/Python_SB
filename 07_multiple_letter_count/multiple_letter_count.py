def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    i = 0
    answer = {}
    while i < len(phrase):
        y = phrase[i]
        x = phrase.count(y)
        answer[y] = x
        i = i + 1
    print(answer)


multiple_letter_count('yay')
multiple_letter_count('Yay')
