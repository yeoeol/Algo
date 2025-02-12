def solution(triangle):
    dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    print(len(triangle))
    for left in range(1, len(triangle)):
        dp[left][0] = dp[left-1][0]+triangle[left][0]
    for right in range(1, len(triangle)):
        dp[right][-1] = dp[right-1][-1]+triangle[right][-1]

    for i in range(2, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    
    return max(dp[-1])