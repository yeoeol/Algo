import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()

def calc(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def solution(n, arr):
    x, y = arr[0]
    tx, ty = arr[-1]
    conv = arr[1:len(arr)-1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited = [False]*len(conv)

        while queue:
            x, y = queue.popleft()
            if calc(tx, ty, x, y) <= 1000:
                return True

            for i, (cx, cy) in enumerate(conv):
                if visited[i]:
                    continue
                if calc(x, y, cx, cy) <= 1000:
                    visited[i] = True
                    queue.append((cx, cy))
                    
        return False

    if bfs(x, y):
        return "happy"
    return "sad"


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n+2)]
    print(solution(n, arr))
