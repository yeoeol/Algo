from functools import cmp_to_key

n = int(input())
serial_nums = [input() for _ in range(n)]

def my_cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1

    cnt1 = 0
    for i in a:
        if not ('A' <= i <= 'Z'):
            cnt1 += int(i)
    cnt2 = 0
    for i in b:
        if not ('A' <= i <= 'Z'):
            cnt2 += int(i)
    if cnt1 < cnt2:
        return -1
    elif cnt1 > cnt2:
        return 1

    for i in range(len(a)):
        if not ('A' <= a[i] <= 'Z') and ('A' <= b[i] <= 'Z'):
            return -1
        elif ('A' <= a[i] <= 'Z') and not ('A' <= b[i] <= 'Z'):
            return 1
        else:
            n1 = ord(a[i])
            n2 = ord(b[i])
            if n1 == n2:
                continue
            elif n1 < n2:
                return -1
            else:
                return 1


serial_nums.sort(key=cmp_to_key(my_cmp))
print(*serial_nums, sep='\n')

