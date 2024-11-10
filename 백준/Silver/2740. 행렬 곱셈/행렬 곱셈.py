A = []
B = []
N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0]*K for _ in range(N)]

for k in range(N):
    for i in range(K):
        for j in range(M):
            C[k][i] += A[k][j]*B[j][i]

for i in C:
    print(*i)
