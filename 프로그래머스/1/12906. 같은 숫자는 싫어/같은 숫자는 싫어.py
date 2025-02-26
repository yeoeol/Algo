def solution(arr):
    answer = []
    prev = arr[0]
    for i in range(1, len(arr)):
        if prev != arr[i]:
            prev = arr[i]
        else:
            arr[i] = -1
    
    for i in range(len(arr)):
        if arr[i] != -1:
            answer.append(arr[i])
    return answer