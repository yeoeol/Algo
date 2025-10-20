n = int(input())
ans = ""
for i in range(1, n+1):
    d = (2*n-1)-(2*i-1)
    print(' '*(d//2), end='')
    print('*'*(2*i-1))
