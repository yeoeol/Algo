from collections import defaultdict

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# A의 부 배열의 합 + B의 부 배열의 합 = t가 되는 부 배열 쌍의 개수
dic_a = defaultdict(int)
for i in range(n):
    sum_val = 0
    for j in range(i, n):
        sum_val += A[j]
        dic_a[sum_val] += 1

ans = 0
for i in range(m):
    sum_val = 0
    for j in range(i, m):
        sum_val += B[j]
        if t-sum_val in dic_a:
            ans += dic_a[t-sum_val]

print(ans)
