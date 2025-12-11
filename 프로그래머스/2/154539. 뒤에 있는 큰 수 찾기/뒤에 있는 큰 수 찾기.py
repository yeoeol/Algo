def solution(numbers):
    n = len(numbers)
    ans = [-1]*n
    stack = []
    
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            ans[stack.pop()] = numbers[i]
            
        stack.append(i)
        
    return ans
