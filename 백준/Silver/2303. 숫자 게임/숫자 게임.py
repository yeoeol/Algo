n = int(input())
ans = []
for _ in range(n):
    arr = list(map(int, input().split()))
    res = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                _sum = arr[i] + arr[j] + arr[k]
                res = max(_sum%10, res)
    ans.append(res)
max_val = max(ans)
real_ans = []
for i in range(len(ans)-1, -1, -1):
    if ans[i] == max_val:
        real_ans.append(i)

if len(real_ans) >= 2:
    print(max(real_ans)+1)
else:
    print(real_ans[0]+1)