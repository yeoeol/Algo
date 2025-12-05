def is_possible(diffs, times, limit, level):
    total_time = 0
    for i in range(len(diffs)):
        time_cur = times[i]
        time_prev = times[i-1]
        if (i-1) < 0:
            time_prev = 0
            
        if diffs[i] <= level:
            total_time += time_cur
        else:
            cnt = diffs[i]-level
            total_time += (time_cur+time_prev)*cnt + time_cur
        if total_time > limit:
            return False
    return True
    
    

def solution(diffs, times, limit):
    i, j = 1, 100000
    while i <= j:
        m = (i+j)//2 
        if is_possible(diffs, times, limit, m):
            j = m-1
        else:
            i = m+1
    return i

