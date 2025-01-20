from collections import deque

def solution(n):
    a = deque()
    while n != 0:
        a.appendleft(n % 3)
        n = n // 3
    while 0 in a:
        for i in range(1, len(a)):
            if a[i] == 0:
                a[i] = 4
                if a[i-1] == 4:
                    a[i-1] = 2
                elif a[i-1] == 2:
                    a[i-1] = 1
                elif a[i-1] == 1:
                    a[i-1] = 0
        if a[0] == 0:
            a.popleft()
    answer = ''
    for i in a:
        answer += str(i)
    return answer