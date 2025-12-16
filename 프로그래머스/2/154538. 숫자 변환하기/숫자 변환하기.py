from collections import deque

def solution(x, y, n):
    visited = set()
    visited.add(x)
    queue = deque()
    queue.append((x, 0))
    
    while queue:
        x, cnt = queue.popleft()
        if x == y:
            return cnt
        for val in [x+n, x*2, x*3]:
            if val <= y and val not in visited:
                visited.add(val)
                queue.append((val, cnt+1))
        
    return -1