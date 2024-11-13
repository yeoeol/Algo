k = int(input())
arr = {}

M = -1
M2 = -1
prev_dir = 0
prev_length = 0
small_rectangle = 250000
one = False
flag = False
for i in range(6):
    d, length = map(int, input().split())
    arr[i] = length
    flag = False
    if prev_dir == 1 and d == 3:
        flag = True
        one = True
    elif prev_dir == 2 and d == 4:
        flag = True
        one = True
    elif prev_dir == 3 and d == 2:
        flag = True
        one = True
    elif prev_dir == 4 and d == 1:
        flag = True
        one = True
    if flag:
        small_rectangle = min(prev_length*length, small_rectangle)
    if d == 1 or d == 2:
        M = max(M, length)
    elif d == 3 or d == 4:
        M2 = max(M2, length)
    prev_dir = d
    prev_length = length
    
if not one:
    small_rectangle = arr.get(0)*arr.get(5)
print((M*M2-small_rectangle)*k)
