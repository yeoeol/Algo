import sys

def solution(info, n, m):
    answer = sys.maxsize
    
    k = len(info)
    visited = set()
    
    def dfs(a_cnt, b_cnt, i=0):
        nonlocal answer
        
        if a_cnt >= n or b_cnt >= m:
            return
        
        if (a_cnt, b_cnt, i) in visited:
            return
        
        visited.add((a_cnt, b_cnt, i))
        
        if i == k:
            answer = min(answer, a_cnt)
            return
        
        na = a_cnt+info[i][0]
        nb = b_cnt+info[i][1]
        
        dfs(na, b_cnt, i+1)
        dfs(a_cnt, nb, i+1)
    
    dfs(0, 0)
    if answer >= n:
        return -1
    else:
        return answer
