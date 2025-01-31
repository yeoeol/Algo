from collections import deque

def solution(rows, columns, queries):
    arr = []
    n = 1
    for i in range(rows):
        arr.append([j for j in range(n, columns+n)])
        n += columns
    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        tmp = deque()
        # 위쪽 행 ( -> )
        for j in range(y1, y2):
            tmp.append(arr[x1][j])
        # 오른쪽 열 ( ↓ )
        for j in range(x1, x2):
            tmp.append(arr[j][y2])
        # 왼쪽 행 ( <- )
        for j in range(y2, y1, -1):
            tmp.append(arr[x2][j])
        # 왼쪽 열 ( ↑ )
        for j in range(x2, x1, -1):
            tmp.append(arr[j][y1])

        tmp.rotate(1)
        answer.append(min(tmp))
        # 위쪽 행 ( -> )
        for j in range(y1, y2):
            arr[x1][j] = tmp.popleft()
        # 오른쪽 열 ( ↓ )
        for j in range(x1, x2):
            arr[j][y2] = tmp.popleft()
        # 왼쪽 행 ( <- )
        for j in range(y2, y1, -1):
            arr[x2][j] = tmp.popleft()
        # 왼쪽 열 ( ↑ )
        for j in range(x2, x1, -1):
            arr[j][y1] = tmp.popleft()

    return answer