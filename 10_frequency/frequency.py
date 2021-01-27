def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    i = 0
    count = 0
    x = len(lst)
    while i < x:
        if lst[i] == search_term:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
    print(count)


frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)
