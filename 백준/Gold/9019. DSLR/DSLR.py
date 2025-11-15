import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def d(n):
    return (n*2)%10000

def s(n):
    if n == 0:
        return 9999
    else:
        return n-1

def l(n):
    return (n % 1000) * 10 + (n//1000)

def r(n):
    return (n % 10) * 1000 + (n//10)


def bfs(a, b, visited):
    queue = deque()
    queue.append(a)

    while queue:
        cur = queue.popleft()
        if cur == b:
            path = ""
            temp_cur = b
            while temp_cur != a:
                parent, order = visited[temp_cur]
                path = order + path
                temp_cur = parent
            return path

        d_val = d(cur)
        s_val = s(cur)
        l_val = l(cur)
        r_val = r(cur)
        if visited[d_val] is None:
            visited[d_val] = (cur, 'D')
            queue.append(d_val)
        if visited[s_val] is None:
            visited[s_val] = (cur, 'S')
            queue.append(s_val)
        if visited[l_val] is None:
            visited[l_val] = (cur, 'L')
            queue.append(l_val)
        if visited[r_val] is None:
            visited[r_val] = (cur, 'R')
            queue.append(r_val)

t = int(input())
ans = []
for _ in range(t):
    a, b = map(int, input().split())
    visited = [None]*10001
    visited[a] = (-1, "")
    ans.append(bfs(a, b, visited))

print('\n'.join(ans))
