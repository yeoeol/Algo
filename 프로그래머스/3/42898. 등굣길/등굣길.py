def solution(m, n, puddles):
    # dp[i][j]: (i, j)까지 가는 경로의 수
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  # 시작점

    # 물웅덩이를 set에 저장 (빠른 조회를 위해)
    puddles_set = {(py - 1, px - 1) for px, py in puddles}

    # 첫 번째 열 초기화 (물웅덩이 만나면 이후는 갈 수 없음)
    for x in range(n):
        if (x, 0) in puddles_set:
            break
        dp[x][0] = 1

    # 첫 번째 행 초기화 (물웅덩이 만나면 이후는 갈 수 없음)
    for y in range(m):
        if (0, y) in puddles_set:
            break
        dp[0][y] = 1

    # DP 테이블 채우기
    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in puddles_set:  # 물웅덩이이면 스킵
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[-1][-1]