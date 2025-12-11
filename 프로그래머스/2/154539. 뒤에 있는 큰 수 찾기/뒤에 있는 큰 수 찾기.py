def solution(numbers):
    n = len(numbers)
    ans = [0]*n
    stack = [(0, numbers[0])]
    
    i = 1
    while stack and i < n:
        if numbers[i] < stack[-1][1]:
            stack.append((i, numbers[i]))
        else:
            while i < n and stack and numbers[i] > stack[-1][1]:
                idx, num = stack.pop()
                ans[idx] = numbers[i]
            stack.append((i, numbers[i]))
        i += 1
    for idx, _ in stack:
        ans[idx] = -1
    return ans
    