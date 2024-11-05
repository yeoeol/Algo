n, m = map(int, input().split())
array_2d = [] # 2차원 배열 저장
for _ in range(n):
    tmp = list(map(int, input().split()))
    array_2d.append(tmp)

dp = [[0]*(m+1) for _ in range(n+1)] # 메모제이션 DP 리스트 생성
# dp[a][b] = array_2d에서 인덱스 (a-1, b-1)까지 모두 더한 값

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = array_2d[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        # ex dp[2][2] = array_2d[0:1][0:1]의 합
        
t = int(input())
for _ in range(t):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]) # i-1, j-1을 빼주어야 i, j부터 남음