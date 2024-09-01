s = input()
q = int(input())

for _ in range(q):
    a, l, r = input().split()
    _sum = 0
    for i in range(int(l), int(r)+1):
        if s[i] == a:
            _sum += 1
    print(_sum)
