depth = 1

def start(n):
    return n-depth if (n-depth >= 0) else 0

def end(n, max_n):
    return n+depth+1 if (n+depth+1 <= max_n) else max_n

def count_neighbours(grid, n, m):
    point = (n,m)
    count = 0
    n_max = len(grid)
    m_max = len(grid[0])

    for i in range(start(n), end(n, n_max)):
        for j in range(start(m), end(m, m_max)):
            curr = (i,j)
            if ( (curr != point) and (grid[i][j] == 1) ):
                count += 1
    print 'count = %d' % count
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
