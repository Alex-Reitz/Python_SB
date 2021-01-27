def triple_and_filter(nums):

    newList = [val for val in nums if val % 4 == 0]
    print(newList)
    answerList = [val*3 for val in newList]
    print(answerList)
    return answerList
    """Return new list of tripled nums for those nums divisible by 4.

        Return every number in list that is divisible by 4 in a new list,
        except multipled by 3.

            >>> triple_and_filter([1, 2, 3, 4])
            [12]

            >>> triple_and_filter([6, 8, 10, 12])
            [24, 36]

            >>> triple_and_filter([1, 2])
            []
        """


triple_and_filter([1, 2, 3, 4])
triple_and_filter([6, 8, 10, 12])
