origin_s = list(input())

result = []
for i in range(1, len(origin_s)+1):
    for j in range(i+1, len(origin_s)):
        f = origin_s[:i]
        s = origin_s[i:j]
        t = origin_s[j:]
        f.reverse()
        s.reverse()
        t.reverse()
        result.append("".join(f)+"".join(s)+"".join(t))
result.sort()
print(result[0])