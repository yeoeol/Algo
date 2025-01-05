import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().strip().split())
    if a == 1:
        print(1)
    else:
        init = a
        lst = []
        while True:
            i = init%10
            if i not in lst:
                lst.append(i)
            else:
                break
            init *= a
        value = lst[(b%len(lst))-1]
        if value == 0:
            print(10)
        else:
            print(value)
