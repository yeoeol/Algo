import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
sum_n = sum(range(1, int(n)))
numbers = input()

sum_num = 0
temp = ""

for num in numbers:
    if num.isdigit():
        temp += num
    else:
        sum_num += int(temp)
        temp = ""

# 마지막 숫자의 처리
sum_num += int(temp)

print(sum_num - sum_n)