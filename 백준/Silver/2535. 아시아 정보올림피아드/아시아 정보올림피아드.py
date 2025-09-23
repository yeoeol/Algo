n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[2], reverse=True)

max_n = max(arr, key=lambda x:x[0])[0]
cnt = [0 for _ in range(max_n+1)]

res = 0
for nation, num, score in arr:
    if cnt[nation] >= 2:
        continue
    cnt[nation] += 1
    res += 1
    
    print(nation, num)
    if res >= 3:
        break
        
