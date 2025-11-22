def solution(mats, grid):
    answer = 0
    mats.sort(reverse=True)
    for mat in mats:
        for i in range(len(grid)-mat+1):
            for j in range(len(grid[0])-mat+1):
                if grid[i][j] == '-1':
                    if all(grid[x][y] == '-1' for x in range(i, i+mat) for y in range(j, j+mat)):
                        return mat
    return -1