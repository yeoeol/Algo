import sys

input = sys.stdin.readline

N, M, B = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip().split())) for i in range(N)]

height = 0
answer = sys.maxsize
for a in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > a:
                exceed_block += arr[i][j] - a
            else:
                lack_block += a-arr[i][j]
    if (exceed_block + B) >= lack_block:
        if (exceed_block*2)+lack_block <= answer:
            answer = (exceed_block*2)+lack_block
            height = a

print(answer, height)