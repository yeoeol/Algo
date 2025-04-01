n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = [0]*m
count[0] = 1

ans = 0
prefix = 0
# 같은 나머지를 가진 누적 합을 가진 두 인덱스를 선택하면
# 부분 합이 M으로 나누어 떨어짐
# (prefix[j]-prefix[i])%m == 0 | ==> prefix[j] % m == prefix[i] % m
for i in range(n):
    prefix += arr[i]
    remainder = prefix % m

    ans += count[remainder]

    count[remainder] += 1

print(ans)