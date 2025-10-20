n = int(input())
for i in range(1, n):
    s = '*'*i
    s += ' '*(2*n-2*i)
    s += '*'*i
    print(s)
for i in range(n, 0, -1):
    s = '*'*i
    s += ' '*(2*n-2*i)
    s += '*'*i
    print(s)
