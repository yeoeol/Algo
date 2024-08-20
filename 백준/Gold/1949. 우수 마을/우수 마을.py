import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
people_nums = ['']+list(map(int, input().split()))
dp = [[0, 0]] + [[0, people_nums[i]] for i in range(1, n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
def dfs(s):
    visited[s] = True
    for i in tree[s]:
        if not visited[i]:
            dfs(i)
            dp[s][1] += dp[i][0]
            dp[s][0] += max(dp[i][1], dp[i][0])

dfs(1)
print(max(dp[1]))