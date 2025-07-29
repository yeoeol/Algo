import itertools

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for a in itertools.permutations(arr, n):
    kg = 500
    for item in a:
        kg += item
        kg -= k
        if kg < 500:
            break
    else:
        ans += 1
print(ans)