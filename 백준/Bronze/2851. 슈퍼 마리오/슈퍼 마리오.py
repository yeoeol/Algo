# 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없음
import sys

arr = []
for _ in range(10):
    arr.append(int(input()))

prefix_sum = [0 for _ in range(10)]
prefix_sum[0] = arr[0]
for i in range(1, 10):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
ans = 0
val = sys.maxsize
for i in range(10):
    if abs(100-prefix_sum[i]) <= val:
        ans = prefix_sum[i]
        val = abs(100-prefix_sum[i])
        
print(ans)