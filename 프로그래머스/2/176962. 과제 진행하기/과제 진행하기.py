def time_to_min(s):
    h, m = map(int, s.split(":"))
    return h*60 + m

def solution(plans):
    lst = []
    for name, start, play in plans:
        lst.append([time_to_min(start), name, int(play)])
    lst.sort()
    
    ans = []
    stack = []  # [name, 남은 시간]
    cur_time = lst[0][0]
    stack.append([lst[0][1], lst[0][2]])
    
    for i in range(1, len(lst)):
        next_start, next_name, next_play = lst[i]
        
        # 현재 시간에 잠깐 멈췄던 과제의 남은 시간을 더한 것이 다음 과제의 시작 시간보다 작거나 같을 때
        while stack and cur_time+stack[-1][1] <= next_start:
            remain_name, remain_time = stack.pop()
            ans.append(remain_name)
            cur_time += remain_time
            
        if stack:
            stack[-1][1] -= (next_start-cur_time)
        
        stack.append([next_name, next_play])
        cur_time = next_start
        
    while stack:
        name, _ = stack.pop()
        ans.append(name)
    return ans