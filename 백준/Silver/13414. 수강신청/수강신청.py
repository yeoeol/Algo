import sys
input = sys.stdin.readline

k, l = map(int, input().strip().split())
dic = {}
for i in range(l):
    num = input().strip()
    dic[num] = i

result = sorted(dic.items(), key=lambda x:x[1])
if k > len(result):
    k = len(result)
    
for i in range(k):
    print(result[i][0])