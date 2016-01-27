# duplicate one digit to maximize the number

def solution(X):
    X_str = str(X)
    sig_dig = -1
    index = 0

    for dig in X_str:
        if dig > sig_dig:
            print dig
            sig_dig = dig
            sig_ind = index
        index += 1
    new_X = X_str[:sig_ind] + sig_dig + X_str[sig_ind:]

solution(12511)
