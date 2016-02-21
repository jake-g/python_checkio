def count_inversion(seq):
    """""""""""""""""""""""""""""""""""""""""""""
    Count inversions in a sequence of numbers
    """""""""""""""""""""""""""""""""""""""""""""
    ls  = list(seq)
    count = 0
    for i in range(1, len(ls)):     
        val = ls[i]
        pos = i

        while pos > 0 and ls[pos - 1] > val:
            ls[pos] = ls[pos - 1]
            pos = pos - 1
            count += 1

        ls[pos] = val
    print count
    return count

if __name__ == '__main__':
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"

