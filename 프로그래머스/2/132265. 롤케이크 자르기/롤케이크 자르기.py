from collections import Counter

def solution(topping):
    n = len(topping)
    
    answer = 0
    counter = Counter(topping)
    
    left = set()
    right = set(topping)
    
    for i in range(n):
        num = topping[i]
        left.add(num)
        counter[num] -= 1
        if counter[num] == 0:
            right.remove(num)
        if len(left) == len(right):
            answer += 1
        
    return answer