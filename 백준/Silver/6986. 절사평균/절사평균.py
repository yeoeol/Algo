import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
arr = [float(input()) for _ in range(n)]
arr.sort()


def func1(arr):
    new_arr = arr[k:-k]
    return sum(new_arr)/len(new_arr)

def func2(arr):
    new_arr = arr[:]
    for i in range(k):
        new_arr[i] = new_arr[k]
        new_arr[-i-1] = new_arr[-k-1]
    return sum(new_arr)/len(new_arr)

if k == 0:
    s = sum(arr)/len(arr)
    print(f"{s:.2f}")
    print(f"{s:.2f}")
else:
    print(f"{func1(arr) + 0.00000001:.2f}")
    print("%.2f"%(func2(arr) + 0.00000001))