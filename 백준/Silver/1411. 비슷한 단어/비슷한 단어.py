n = int(input())
words = [input() for _ in range(n)]

def check(x):
    cnt = dict()
    pattern = []

    next_num = 0
    for ch in x:
        if ch not in cnt:
            cnt[ch] = next_num
            next_num += 1
        pattern.append(cnt[ch])
    return pattern

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if check(words[i]) == check(words[j]):
            ans += 1
print(ans)
