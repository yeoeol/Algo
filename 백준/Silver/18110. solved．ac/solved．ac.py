import sys
input = sys.stdin.readline

def my_round(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    return int(x)

n = int(input().strip())
if n == 0:
    print(0)
    exit(0)
exception = my_round(n*0.3/2)

level = [int(input().strip()) for i in range(n)]

level = sorted(level)
level = level[exception:n-exception]

avg = my_round(sum(level)/len(level))
print(avg)