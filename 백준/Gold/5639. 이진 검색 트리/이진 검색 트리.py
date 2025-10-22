import sys
sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        arr.append(int(input()))
    except EOFError:
        break

def get_post_order(lst):
    if len(lst) == 0:
        return
    root = lst[0]
    left, right = [], []
    for i in range(1, len(lst)):
        if lst[i] < root:
            left.append(lst[i])
        else:
            right.append(lst[i])
    get_post_order(left)
    get_post_order(right)
    print(root)

get_post_order(arr)