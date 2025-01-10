a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
lst.reverse()

ten = 0
for i in range(m):
    ten += lst[i]*(a**i)

result = []
while ten != 0:
    remainder = ten % b
    ten = ten // b
    result.append(remainder)
result.reverse()
print(' '.join(map(str, result)))
