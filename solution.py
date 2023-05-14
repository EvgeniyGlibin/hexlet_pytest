def invert_case(string):
    # BEGIN (write your solution here)
    """ Invert string
    >>> invert_case
    """
    # END

    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()


print(invert_case('hello'))