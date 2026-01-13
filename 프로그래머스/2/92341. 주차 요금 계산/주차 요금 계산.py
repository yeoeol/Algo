from collections import defaultdict
import math

def time_to_min(hm):
    split = hm.split(":")
    h = int(split[0])
    m = int(split[1])
    return h*60+m
    

def solution(fees, records):
    dic = dict()
    car_time = defaultdict(int)
    
    for record in records:
        time, car_num, rec = record.split(' ')
        t = time_to_min(time)
        if rec == "IN":
            dic[car_num] = t
        else:
            car_time[car_num] += t-dic[car_num]
            del dic[car_num]
    for car_num in dic:
        t = time_to_min("23:59")
        car_time[car_num] += t-dic[car_num]
    
    ans = []
    for key in sorted(car_time.keys()):
        time = car_time[key]
        if time <= fees[0]:
            ans.append(fees[1])
        else:
            exceed_time = time-fees[0]
            f = fees[1] + math.ceil(exceed_time/fees[2])*fees[3]
            ans.append(f)
    return ans