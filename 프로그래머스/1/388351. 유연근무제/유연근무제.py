def func(hope, arr, startday):
    for i in range(len(arr)):
        if 1 <= startday <= 5:
            if arr[i] > hope:
                return False
        startday += 1
        if startday == 8:
            startday = 1
    return True

def plus_ten_min(t):
    if t % 100 >= 50:
        return ((t // 100)+1)*100 + (((t%100)+10)%60)
    else:
        return t + 10

def solution(sc, tl, startday):
    answer = 0
    for i in range(len(sc)):
        temp = plus_ten_min(sc[i])
        if func(temp, tl[i], startday):
            answer += 1
    
    return answer