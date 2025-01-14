n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

nums = [set() for _ in range(n)]

# 0 0
# 1 0
# 2 0
# 3 0
# 4 0
# 0 1
# 1 1
# 2 1

for k in range(5):
    for i in range(n):
        target = lst[i][k]
        for j in range(i+1, n):
            if target == lst[j][k]:
                nums[i].add(j)
                nums[j].add(i)

result = []
M = max(len(i) for i in nums)
for i in range(n):
    if M == len(nums[i]):
        result.append(i)
print(result[0]+1)
