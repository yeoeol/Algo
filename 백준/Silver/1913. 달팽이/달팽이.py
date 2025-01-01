n = int(input())
find_num = int(input())

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
table = [[0] * n for _ in range(n)]
target_position = (0, 0)

x, y = n//2, n//2
if find_num == 1:
    target_position = (x+1, y+1)
table[x][y] = 1

num = 2
step = 1  # 한 방향으로 이동할 칸 수
while num <= n * n:
    for direction in range(4):
        for _ in range(step):
            if num > n * n:
                break
            x += d[direction][0]
            y += d[direction][1]
            table[x][y] = num
            if num == find_num:
                target_position = (x+1, y+1)
            num += 1
        if direction == 1 or direction == 3:    # 우측이나 하단 이동 후에는 step 증가
            step += 1

for i in table:
    print(*i)
print(*target_position)