from collections import deque


def check_count(grid, x, y):
    cnt = 1
    for i in range(x-1, -1, -1):
        if grid[i][y] == 0:
            return cnt
        cnt += 1
    return cnt

def solution(n, w, num):
    answer = 0
    k = n//w if n % w == 0 else n//w+1
    grid = [deque() for _ in range(k)]
    idx = k-1
    
    cnt = 0
    right = True
    for i in range(1, n+1):
        if right:
            grid[idx].append(i)
        else:
            grid[idx].appendleft(i)
        cnt += 1
        if cnt == w:
            idx -= 1
            cnt = 0
            right = not right
    if right:
        for _ in range(w-len(grid[0])):
            grid[0].append(0)
    else:
        for _ in range(w-len(grid[0])):
            grid[0].appendleft(0)
            
    flag = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == num:
                answer = check_count(grid, i, j)
                flag = True
                break
        if flag:
            break
    return answer