lst = [1, 2, 3]


def list_manipulation(lst, command, location, value=None):
    if command == "add" and location == "beginning":
        print(lst.insert(0, value))
    elif command == "add" and location == "end":
        print(lst.append(value))

    elif command == "remove" and location == "beginning":
        print(lst.pop(0))
    elif command == "remove" and location == "end":
        print(lst.pop())

    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """


""" list_manipulation(lst, 'remove', 'end') """
""" list_manipulation(lst, 'remove', 'beginning') """
""" list_manipulation(lst, 'add', 'beginning', 20) """
list_manipulation(lst, 'add', 'end', 30)
