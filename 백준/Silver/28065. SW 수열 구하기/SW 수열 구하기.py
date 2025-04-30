n = int(input())
arr = [0 for _ in range(n)]
# 앞 차이가 뒤 차이보다 큰 수열
# 4 1 3 2
#
# 5 1 4 2 3

num1 = n
num2 = 1
for i in range(n):
    if i % 2 == 0:
        arr[i] = num1
        num1 -= 1
    else:
        arr[i] = num2
        num2 += 1
print(*arr)