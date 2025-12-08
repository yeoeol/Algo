def solution(h1, m1, s1, h2, m2, s2):
    # 시침은 1초에 1/120도
    # 분침은 1초에 0.1도
    # 초침은 1초에 6도
    start = h1*3600+m1*60+s1
    end = h2*3600+m2*60+s2
    cnt = 0
    if start == 0 or start == 12*3600:
        cnt += 1
        
    for t in range(start, end):
        hour = t*(1/120)%360
        minute = t*(0.1)%360
        seconds = (t*6)%360
        
        hour2 = (t+1)*(1/120)%360
        if hour2 == 0: hour2 = 360
        
        minute2 = (t+1)*(0.1)%360
        if minute2 == 0: minute2 = 360
        
        seconds2 = ((t+1)*6)%360
        if seconds2 == 0: seconds2 = 360
        
        # 초침이 분침을 지나거나 겹치는 경우
        if seconds < minute and seconds2 >= minute2:
            cnt += 1
        # 초침이 시침을 지나거나 겹치는 경우
        if seconds < hour and seconds2 >= hour2:
            cnt += 1
            
        if (seconds < minute and seconds2 >= minute2) and (seconds < hour and seconds2 >= hour2):
            if minute2 == hour2:
                cnt -= 1
        
    return cnt