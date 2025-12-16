from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque()
    queue.append((x, 0))
    while queue:
        x, cnt = queue.popleft()
        if x > 1000000:
            continue
        if x == y:
            return cnt
        if x not in visited:
            visited.add(x)
            queue.append((x+n, cnt+1))
            queue.append((x*2, cnt+1))
            queue.append((x*3, cnt+1))
        
    return -1