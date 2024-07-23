import sys
import collections

input = sys.stdin.readline
MAX = 10**5

n, k = map(int, input().split())
dist = [0]*(MAX+1)

def bfs():
    queue = collections.deque()
    queue.append(n)
    while queue:
        p = queue.popleft()
        if p == k:
            print(dist[p])
            return
        for nxt in (p-1, p+1, p*2):
            if 0 <= nxt <= MAX and dist[nxt] == 0:
                dist[nxt] = dist[p]+1
                queue.append(nxt)

bfs()