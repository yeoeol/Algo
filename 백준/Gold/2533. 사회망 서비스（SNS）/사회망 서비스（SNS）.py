import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline



n = int(input().rstrip())
tree = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

# 본인 자식이 얼리어답터일 경우 본인도 얼리어답터 (루트 노드 제외)
# 본인의 자식이 모두 리프노드일 경우 본인 얼리어답터
# => DP[현재 노드] =
# MIN( DP[내 자식 노드들][ 얼리어답터인 경우 최적해] , DP[내 자식 노드들][ 얼리어답터가 아닌 경우 최적해 )


visited = [0] * (n+1)
def dfs(s):
    visited[s] = 1
    if len(tree[s]) == 0:
        dp[s][0] = 0
        dp[s][1] = 1
    else:
        for i in tree[s]:
            if visited[i] == 0:
                dfs(i)
                dp[s][1] += min(dp[i][1], dp[i][0])
                dp[s][0] += dp[i][1]
        dp[s][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))