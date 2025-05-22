n = list(input())
if n.count('0') == 0 or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    n.sort(reverse=True)
    print(''.join(n))