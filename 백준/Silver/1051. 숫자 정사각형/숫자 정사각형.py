N, M = map(int, input().split())

arr = [input() for _ in range(N)]

size = 1
m_value = min(N, M)
for n in range(N):
    for m in range(M):
        for k in range(1, m_value):
            if ((n+k) < N) and ((m+k) < M) and arr[n][m] == arr[n+k][m+k] == arr[n][m+k] == arr[n+k][m]:
                size = max(size, (k+1)**2)
print(size)