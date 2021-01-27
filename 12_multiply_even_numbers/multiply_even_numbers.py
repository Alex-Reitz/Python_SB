def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>>
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    i = 0
    count = 1

    while i < len(nums):
        if nums[i] % 2 == 0:
            count = count * nums[i]
        i = i + 1
    print(count)


multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
