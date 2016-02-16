import math

# calulate angle opposite to side a
def law_cosine(a, b, c):
    return math.acos((b**2 + c**2 - a**2)/(2*c*b))


def law_sine(a, b, A):
    return math.asin((b*math.sin(A))/a)

def checkio(a, b, c):
    s = [a, b, c]
    A = law_cosine(s[0], s[1], s[2])
    print A
    B = math.sin(math.sin(A)*s[1]/s[0])
    print B
    C = math.pi - A - B
    print C
    print [(180/math.pi)*rad for rad in [A, B, C]]
    # B = law_sine(s[0], s[1], A)
    #replace this for solution
    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
