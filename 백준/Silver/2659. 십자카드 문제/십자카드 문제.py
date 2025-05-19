import sys

arr = input().split()


def func(arr):
    min_val = sys.maxsize
    arr += arr
    for i in range(4):
        min_val = min(min_val, int(''.join(arr[i:i+4])))
    return min_val

target = func(arr)
lst = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                lst.add(func(str(i)+str(j)+str(k)+str(l)))
print(sorted(lst).index(target)+1)