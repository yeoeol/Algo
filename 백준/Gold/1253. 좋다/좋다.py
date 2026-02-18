n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for t in range(n):
    left = 0
    right = n-1

    while left < right:
        if left == t:
            left += 1
            continue
        elif right == t:
            right -= 1
            continue
        if arr[left] + arr[right] == arr[t]:
            answer += 1
            break
        elif arr[left] + arr[right] < arr[t]:
            left += 1
        elif arr[left] + arr[right] > arr[t]:
            right -= 1

print(answer)


