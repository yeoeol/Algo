from collections import deque

queue = deque()

def bfs(numbers, target):
    ans = 0
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))
    while queue:
        x, i = queue.popleft()
        if i >= len(numbers):
            if x == target:
                ans += 1
            continue
        queue.append((x+numbers[i], i+1))
        queue.append((x-numbers[i], i+1))

    return ans

def solution(numbers, target):
    cnt = bfs(numbers, target)
    return cnt

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))