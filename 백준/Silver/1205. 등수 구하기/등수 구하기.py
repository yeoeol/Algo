n, new_score, p = map(int, input().split())
if n == 0:
    print(1)
    exit(0)
rank_score = list(map(int, input().split()))
idx = 0
for i in range(n):
    if rank_score[i] < new_score:
        rank_score.insert(i, new_score)
        idx = i
        break
else:
    rank_score.append(new_score)
    idx = n

if idx >= p:
    print(-1)
    exit(0)
if len(rank_score) > p:
    rank_score = rank_score[:p]
rank = [-1 for _ in range(p)]
rank[0] = 1
add = 1
for i in range(1, len(rank_score)):
    if rank_score[i-1] == rank_score[i]:
        add += 1
        rank[i] = rank[i-1]
    else:
        rank[i] = rank[i-1]+add
        add = 1
print(rank[idx])

