import math


def checkio(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        C = round(math.acos((a**2 + b**2 - c**2) / float(2 * a * b)) * 180 / math.pi)
        B = round(math.acos((a**2 + c**2 - b**2) / float(2 * a * c)) * 180 / math.pi)
        A = 180 - (B + C)
        return sorted([A, B, C])
    else:
        return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(4, 3, 5) == [37, 53, 90], "Egyptian triangle"

