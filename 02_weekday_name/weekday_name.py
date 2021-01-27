def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    i = 0
    weekdays = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

    while i < len(weekdays):
        if i + 1 == day_of_week:
            print(weekdays[i])
        i = i + 1


weekday_name(1)
weekday_name(2)
weekday_name(3)
weekday_name(4)
