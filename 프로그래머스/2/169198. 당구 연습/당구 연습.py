import sys
import math


def calc(x, y, ex, ey):
    return (x-ex)**2+(y-ey)**2

def solution(m, n, startX, startY, balls):
    ans = []
    for x, y in balls:
        res = sys.maxsize
        ux, uy = x, n+(n-y)
        rx, ry = m+(m-x), y
        dx, dy = x, -y
        lx, ly = -x, y
        
        for i, (nx, ny) in enumerate([(ux, uy), (rx, ry), (dx, dy), (lx, ly)]):
            # 세로선이 같을 때 x < startX 라면 왼쪽X
            if y == startY and x < startX and i == 3:
                continue
            elif y == startY and x > startX and i == 1:
                continue
            elif x == startX and y < startY and i == 2:
                continue
            elif x == startX and y > startY and i == 0:
                continue
                
            res = min(res, calc(startX, startY, nx, ny))
        ans.append(res)
    return ans
        