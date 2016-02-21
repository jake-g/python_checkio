def insertation_sort(ls):
    for i in range(1, len(ls)):     
        val = ls[i]
        pos = i
        while pos > 0 and ls[pos - 1] > val:
            ls[pos] = ls[pos - 1]
            pos = pos - 1
        ls[pos] = val
    return ls

if __name__ == '__main__':
    assert insertation_sort([1, 2, 5, 3, 4, 7, 6]) == [1, 2, 3, 4, 5, 6, 7]
    assert insertation_sort([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert insertation_sort([99, -99]) == [-99, 99]
    assert insertation_sort([5, 3, 2, 1, 0]) == [0, 1, 2, 3, 5]
print 'SUCCCEESS'
