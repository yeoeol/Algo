def solution(arr):
    answer = []
    prev = arr[0]
    for i in range(1, len(arr)):
        if prev != arr[i]:
            answer.append(prev)
            prev = arr[i]
    answer.append(prev)
    return answer