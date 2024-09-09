n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 하얀색 0, 파란색 1

def rec(x, y, c):
    color = graph[x][y]
    c2 = c//2
    for i in range(x, x+c):
        for j in range(y, y+c):
            if graph[i][j] != color:
                rec(x, y, c2)
                rec(x, y+c2, c2)
                rec(x+c2, y, c2)
                rec(x+c2, y+c2, c2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

result = []
rec(0, 0, n)
print(result.count(0))
print(result.count(1))
