import sys
from collections import deque

n = int(input())
s = input()
nums = deque()
operators = deque()

for i in range(n):
    if s[i].isdecimal():
        nums.append(int(s[i]))
    else:
        operators.append(s[i])

def calc(a, b, o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    else:
        return a*b


max_val = -sys.maxsize
def rec(op_idx, cur):
    global max_val
    if op_idx == len(operators):
        max_val = max(max_val, cur)
        return

    res1 = calc(cur, nums[op_idx+1], operators[op_idx])
    rec(op_idx+1, res1)

    if op_idx+1 < len(operators):
        next_val = calc(nums[op_idx+1], nums[op_idx+2], operators[op_idx+1])
        res2 = calc(cur, next_val, operators[op_idx])
        rec(op_idx+2, res2)

rec(0, nums[0])
print(max_val)

