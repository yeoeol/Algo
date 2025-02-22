from sys import stdin
        
n, k = map(int, stdin.readline().split())
lst = [i for i in range(1, n+1)]
result = []

cnt = 0

for i in range(n):
    cnt = (cnt+k-1)%len(lst)
    result.append(lst.pop(cnt))

print('<'+', '.join(map(str, result))+'>')
