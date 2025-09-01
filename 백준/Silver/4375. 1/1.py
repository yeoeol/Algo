import sys

def input():
    return sys.stdin.readline().strip()


def find(x):
    s = int("1"*len(str(x)))
    while True:
        if s % x == 0:
            return s
        s = s*10+1

while True:
    try:
        n = int(input())
        s = find(n)
        print(len(str(s)))
    except:
        break