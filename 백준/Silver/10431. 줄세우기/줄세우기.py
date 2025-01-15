from collections import deque

p = int(input())
for _ in range(p):
    arr = list(map(int, input().split()))
    t = arr.pop(0)

    q = deque([arr[0]])
    result = 0
    for i in range(1, 20):
        if arr[i] < q[0]:
            result += len(q)
            q.appendleft(arr[i])
        elif arr[i] > q[-1]:
            q.append(arr[i])
        else:
            for j in range(len(q)):
                if arr[i] < q[j]:
                    result += len(q)-j
                    q.insert(j, arr[i])
                    break
    print(t, result)

