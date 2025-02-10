import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    w = []
    for i in works:
        heapq.heappush(w, -i)
    while n > 0:
        M = -heapq.heappop(w)
        M -= 1
        heapq.heappush(w, -M)
        n -= 1

    answer = 0
    for i in w:
        answer += i*i
    return answer