import sys


__version__ = '0.1.0'
__all__ = ['dumps', 'loads']


if sys.version_info.major == 2:
    integer_types = (int, long)
else:
    integer_types = (int,)


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'


def dumps(number):
    """Dumps an integer into a base36 string.

    :param number: the 10-based integer.
    :returns: the base36 string.
    """
    if not isinstance(number, integer_types):
        raise TypeError('number must be an integer')

    if number < 0:
        return '-' + dumps(-number)

    value = ''

    while number != 0:
        number, index = divmod(number, len(alphabet))
        value = alphabet[index] + value

    return value


def loads(value):
    """Loads a base36 string and parse it into 10-based interger.

    :param value: the base36 string.
    :returns: the parsed integer.
    """
    return int(value, 36)