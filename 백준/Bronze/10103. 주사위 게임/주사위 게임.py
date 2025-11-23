n = int(input())
score1 = score2 = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue

    if a < b:
        score1 -= b
    else:
        score2 -= a

print(score1)
print(score2)