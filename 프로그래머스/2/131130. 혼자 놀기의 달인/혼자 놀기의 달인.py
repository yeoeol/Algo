def dfs(cards, idx, visited, cnt):
    if visited[cards[idx]]:
        return cnt
    
    visited[cards[idx]] = True
    return dfs(cards, cards[idx]-1, visited, cnt+1)

def solution(cards):
    # 각 자리마다 열 수 있는 경우의 수를 미리 구해놓고
    # 그 수 중 2개를 골라 곱하여 가장 큰 수를 구하기
    result = []
    visited = [False] * (len(cards)+1)
    for i in range(len(cards)):
        visited[i] = True
        cnt = dfs(cards, i, visited, 0)
        result.append(cnt)
    
    result.sort()
    return result[-1]*result[-2]