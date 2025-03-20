# 주어진 리스트가 올바른 괄호인지 체크
def check(lst):
    stack = []
    for cur in lst:
        if cur == '(':
            stack.append(cur)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True

def choose(open, close, n, lst):
    if open == n and close == n:
        if check(lst):
            return 1
        return 0

    total = 0
    if open < n:
        lst.append('(')
        total += choose(open+1, close, n, lst)
        lst.pop()
    if close < open:
        lst.append(')')
        total += choose(open, close+1, n, lst)
        lst.pop()
    return total

def solution(n):
    lst = []
    return choose(0, 0, n, lst)
