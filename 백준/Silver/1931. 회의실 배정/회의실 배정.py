n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end = l[0][1]
for i in range(1, n):
    if l[i][0] >= end:
        cnt += 1
        end = l[i][1]
print(cnt)

