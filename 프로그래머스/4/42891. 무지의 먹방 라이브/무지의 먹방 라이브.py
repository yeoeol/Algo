import heapq

def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    
    hq = []
    for i in range(len(food_times)):
        # 음식 시간, 음식 번호
        heapq.heappush(hq, (food_times[i], i+1))
    
    length = len(food_times)
    prev_time = 0
    while (hq[0][0]-prev_time)*length <= k:
        cur_time = heapq.heappop(hq)[0]
        k -= (cur_time-prev_time)*length
        length -= 1
        
        prev_time = cur_time
    
    hq.sort(key=lambda x:x[1])
    return hq[k%length][1]
            
            
            
