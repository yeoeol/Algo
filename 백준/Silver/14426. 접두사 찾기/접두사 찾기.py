import sys


def input():
    return sys.stdin.readline().strip()


n, m = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()

def binary_search(s, word):
    start, end = 0, len(s)-1
    while start <= end:
        mid = (start+end)//2

        if s[mid].startswith(word):
            return True
        elif s[mid] < word:
            start = mid+1
        elif s[mid] > word:
            end = mid-1
    return False

answer = 0
for _ in range(m):
    word = input()
    if binary_search(s, word):
        answer += 1
print(answer)
