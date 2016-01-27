from datetime import date


def checkio(from_date, to_date):
    """
        Count the Sat and Suns in period
    """
    to = to_date.weekday()
    fr = from_date.weekday()
    delta = to_date - from_date
    weeks = delta.days/7
    day = delta.days % 7

    if (day + fr >= 6) and (day != 0):
        return 2*weeks + 2
    elif day + fr >= 5:
        return 2*weeks + 1
    else:
        return 2*weeks

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
    assert checkio(date(2004, 2,1), date(2004,2,29)) == 9, "Last example"


