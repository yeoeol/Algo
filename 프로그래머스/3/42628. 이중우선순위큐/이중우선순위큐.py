import heapq

def solution(operations):
    answer = []

    for op in operations:
        split = op.split(' ')
        order, num = split[0], int(split[1])
        if order == 'I':
            heapq.heappush(answer, num)
        elif order == 'D':
            if not answer:
                continue
            if num == 1:
                # 최댓값 삭제
                answer.remove(max(answer))
            else:
                # 최솟값 삭제
                heapq.heappop(answer)
    if answer:
        return [max(answer), min(answer)]
    return [0, 0]