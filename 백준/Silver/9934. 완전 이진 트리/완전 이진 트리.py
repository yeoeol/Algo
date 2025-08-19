k = int(input())
orders = list(map(int, input().split()))

result = [[] for _ in range(k)]
def dfs(arr, mid, level):
    left, right = arr[:mid], arr[mid+1:]
    result[level].append(left[len(left)//2])
    result[level].append(right[len(right)//2])
    if len(left) == 1 or len(right) == 1:
        return
    dfs(left, len(left) // 2, level + 1)
    dfs(right, len(right) // 2, level + 1)

result[0].append(orders[len(orders)//2])
dfs(orders, len(orders)//2, 1)

for r in result:
    print(*r)