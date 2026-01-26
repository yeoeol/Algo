from collections import deque


def is_success(arr):
    dic = {
        0:'[', ']':0,
        1:'(', ')':1,
        2:'{', '}':2
    }
    stack = []
    for item in arr:
        if item in ['[', '(', '{']:
            stack.append(item)
        else:
            idx = dic[item]
            if stack and stack[-1] == dic[idx]:
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    
    return True


def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        if is_success(s):
            answer += 1
        s.rotate(-1)
    
    return answer