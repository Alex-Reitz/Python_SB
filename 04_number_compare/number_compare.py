def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        print("Numbers are equal")
    elif b > a:
        print("Second is greater")
    else:
        print("First is greater")


number_compare(4, 7)
number_compare(7, 4)
number_compare(7, 7)
