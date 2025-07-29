n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = [False for _ in range(n)]
cnt, ans = 0, 0
def dfs(w):
    global cnt, ans
    if w < 500:
        return
    if cnt == n:
        ans += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(w+arr[i]-k)
            visited[i] = False
            cnt -= 1
dfs(500)
print(ans)