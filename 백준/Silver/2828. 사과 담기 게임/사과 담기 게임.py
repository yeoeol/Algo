n, m = map(int, input().split())
j = int(input())

left, right = 1, m
result = 0

for _ in range(j):
    location = int(input())
    if left > location:     # 사과가 바구니 왼쪽 밖에 있을 때
        result += (left-location)
        left = location
        right = left+m-1
    elif right < location:  # 사과가 바구니 오른쪽 밖에 있을 때
        result += (location-right)
        right = location
        left = right-m+1
    elif left <= location <= right:
        continue

print(result)