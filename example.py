def reverse(string):
    """Reverse string

    >>> reverse('')
    ''

    >>> reverse('Hexlet')
    'telxeH'
    """
    """
    This is the "example" module.

    The example module supplies one function, reverse().  For example,

    >>> reverse('awesome!')
    '!emosewa'
    """
    return string[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()