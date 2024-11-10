def change(num):
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] = 0
    return

switch_num = int(input())
arr = [-1]+list(map(int, input().split()))
student_num = int(input())
for _ in range(student_num):
    a, b = map(int, input().split())
    if a == 1:
        for j in range(b, switch_num+1, b):
            change(j)
    else:
        change(b)
        for j in range(switch_num//2):
            if b-j < 1 or b+j > switch_num: break
            if arr[b-j] == arr[b+j]:
                change(b-j)
                change(b+j)
            else:
                break


for i in range(1, switch_num+1):
    print(arr[i], end = " ")
    if i % 20 == 0:
        print()