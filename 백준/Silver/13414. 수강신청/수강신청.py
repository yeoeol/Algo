import sys
input = sys.stdin.readline

k, l = map(int, input().strip().split())
queue = []
dic = {}
for i in range(l):
    num = input().strip()
    if num in dic.keys():
        queue[dic[num]] = -1
    dic[num] = i
    queue.append(num)

cnt = 0
for i in range(l):
    if queue[i] != -1:
        print(queue[i])
        cnt += 1
        if cnt == k:
            break
