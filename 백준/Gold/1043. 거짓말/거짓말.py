# 진실을 아는 사람과 연결되지 않으면서 최대로 연결 가능한 컴포넌트 개수
n, m = map(int, input().split())
truth = list(map(int, input().split())) # truth[0] 은 사람 수, thuth[1:] 진실을 아는 사람

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

origin = []
for _ in range(m):
    num, *arr = list(map(int, input().split()))
    origin.append(arr)
    for i in range(num-1):
        union(arr[i], arr[i+1])

for i in range(truth[0]-1):
    union(truth[i+1], truth[i+2])


if truth[0] >= 1:
    m_val = find(min(truth[1:]))
else:
    m_val = 0

not_know = []
for i in range(1, n+1):
    if m_val != find(parent[i]):
        not_know.append(i)
    # 진실을 아는 사람 중 가장 작은 번호를 가진 사람과
    # find 값이 다른 사람의 번호만 들어있는 개수 출력

ans = 0
for i in range(m):
    if all(x in not_know for x in origin[i]):
        ans += 1

print(ans)

