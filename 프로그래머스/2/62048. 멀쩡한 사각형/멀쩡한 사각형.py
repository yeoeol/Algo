import math

def solution(w,h):
    # w, h가 서로소라면 w+h-1
    
    # 최대공약수로 나눈 nw, nh를 기준으로 nw+nh-1
    # 최대공약수 * (nw+nh-1)    
    num = math.gcd(w, h)
    nw, nh = w//num, h//num
    return (w*h)-(num*(nw+nh-1))
