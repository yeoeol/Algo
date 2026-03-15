def solution(arr):
    cnt = [0, 0]
    
    def dfs(x, y, l):
        num = arr[x][y]
        flag = False
        for i in range(l):
            for j in range(l):
                if arr[x+i][y+j] != num:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            cnt[arr[x][y]] += 1
            return
        
        dfs(x, y, l//2)
        dfs(x, y+l//2, l//2)
        dfs(x+l//2, y, l//2)
        dfs(x+l//2, y+l//2, l//2)
    
    dfs(0, 0, len(arr))
    
    return cnt