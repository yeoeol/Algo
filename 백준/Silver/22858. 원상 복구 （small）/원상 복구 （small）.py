n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

# s에서 반대로 찾아가기
for _ in range(k):
    temp = [0]*(n+1)
    for i in range(1, n+1):
        idx = d[i]
        temp[idx] = s[i]
    s = temp
print(*s[1:])