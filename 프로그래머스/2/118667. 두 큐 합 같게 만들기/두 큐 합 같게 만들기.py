from collections import deque

def solution(queue1, queue2):
    answer, cnt = 0, 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target_sum = (sum1+sum2)//2
    max_iter = len(queue1)*4
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    if max(queue1) > target_sum or max(queue2) > target_sum or (sum1+sum2) % 2 != 0:
        answer = -1
    else:
        while cnt < max_iter:
            if sum1 == target_sum == sum2:
                break
            if sum1 > target_sum:
                p = deq1.popleft()
                deq2.append(p)
                sum1 -= p
                sum2 += p
            elif sum2 > target_sum:
                p = deq2.popleft()
                deq1.append(p)
                sum1 += p
                sum2 -= p
            answer += 1
            cnt += 1
        if cnt == max_iter:
            answer = -1
    return answer
