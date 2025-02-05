def is_correct_str(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif not stack:
            return False
        else:
            stack.pop()
    if stack:
        return False
    else:
        return True

def divide_str(string):
    u, v = '', ''
    total_left, total_right = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            u += string[i]
            total_left += 1
        elif string[i] == ')':
            u += string[i]
            total_right += 1
        if total_left == total_right:
            v = string[i+1:]
            return u, v

def solution(p):
    if p == '':
        return ''

    u, v = divide_str(p)    # 2
    if is_correct_str(u):   # 3
        u += solution(v)    # 3
        return u            # 3-1
    else:                   # 4
        empty = '('
        empty += solution(v)
        empty += ')'
        u = u[1:-1]
        for item in u:
            if item == '(':
                empty += ')'
            else:
                empty += '('
    return empty