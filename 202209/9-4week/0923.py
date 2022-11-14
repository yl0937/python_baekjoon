
def find_num(n, r, c):
    # 1
    if n == 1:

        return find_q(n, r, c)

    result = find_q(n, r, c)
    # 1
    if result == 0:

        return find_num(n - 1, r, c)
    # 2
    elif result == 1:

        return 2 ** (2 * (n - 1)) * 1 + find_num(n - 1, r, c - 2 ** (n - 1))

    # 3
    elif result == 2:

        return 2 ** (2 * (n - 1)) * 2 + find_num(n - 1, r - 2 ** (n - 1), c)
    #4
    else:

        return 2 ** (2 * (n - 1)) * 3 + find_num(n - 1, r - 2 ** (n - 1), c - 2 ** (n - 1))

def find_q(n, r, c):
    num = 2 ** (n - 1)

    if (r < num) & (c < num):
        return 0
    elif (r < num) & (c >= num):
        return 1
    elif (r >= num) & (c < num):
        return 2
    else:
        return 3


n, r, c = map(int, input().split())

print(find_num(n, r, c))