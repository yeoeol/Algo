n, m = map(int, input().split())
dna = [input() for _ in range(n)]

result = ""
total = 0
for i in range(m):
    fre = [0 for _ in range(27)]
    for j in range(n):
        fre[ord(dna[j][i])-65] += 1
    c = chr(fre.index(max(fre))+65)
    result += c
for i in range(n):
    for j in range(m):
        if dna[i][j] != result[j]:
            total += 1
print(result)
print(total)