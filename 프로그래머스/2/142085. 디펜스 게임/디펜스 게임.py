from heapq import heappush, heappop

def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    hq = []
    # 이전까지의 수 중 가장 큰 수를 계속 기록
    for i in range(len(enemy)):
        heappush(hq, -enemy[i])
        n -= enemy[i]
        
        if n < 0:
            if k == 0:
                return i
            n += -heappop(hq)
            k -= 1
        
    return len(enemy)