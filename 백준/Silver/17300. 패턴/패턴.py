l = int(input())
arr = list(map(int, input().split()))
grid = [[0]*3 for _ in range(3)]

mid = {
    (1, 3):2, (3, 1):2,
    (1, 7):4, (7, 1):4,
    (1, 9):5, (9, 1):5,
    (2, 8):5, (8, 2):5,
    (3, 9):6, (9, 3):6,
    (7, 9):8, (9, 7):8,
    (3, 7):5, (7, 3):5,
    (4, 6):5, (6, 4):5
}

visited = [False]*10
flag = True
prev = arr[0]
visited[prev] = True
for i in range(1, l):
    cur = arr[i]
    if visited[cur]:
        flag = False
        break
    elif (prev, cur) in mid and not visited[mid[(prev, cur)]]:
        flag = False
        break
    visited[cur] = True
    prev = cur
    
print("NO" if not flag else "YES")