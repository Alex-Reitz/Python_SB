def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    i = 0
    lowerWord = word.lower()
    while i < len(lowerWord):
        if lowerWord[i] == letter:
            count = count + 1
        i = i + 1
    print(count)


single_letter_count("aaaaaaaaaaaaaaa", "a")
single_letter_count("Hello World", 'l')
single_letter_count('Hello World', 'z')
single_letter_count('Hello World', 'h')
