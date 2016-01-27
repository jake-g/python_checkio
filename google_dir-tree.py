# return the len of the longest path to an image

def solution(S):
    exts = ['.jpeg', '.png', '.gif']
    dirs = S.split('\n')
    depth = 0
    path = ''
    max_len = 0
    found = False
    space = 0
    for name in dirs:
        if 'dir' in name:
            depth += 1
            if ' '*space in name:
                path = path + '/' + name.strip()
                space += 1

        if any(ext in name for ext in exts):
            path = path + '/' + name.strip()
            found = True
            if len(path) > max_len:
                max_len = len(path)
            path = ''
            depth = 0
    return max_len if (found) else 0



print(solution('dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif'))