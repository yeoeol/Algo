import java.util.*;


class Solution {
    
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    static int N;
    
    static List<List<int[]>> tableCoords = new ArrayList<>();
    
    public int solution(int[][] board, int[][] table) {
        tableCoords.clear();
        N = table.length;
        
        boolean[][] visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && table[i][j] == 1) {
                    List<int[]> coords = new ArrayList<>();
                    coords.add(new int[]{i, j});
                    
                    dfs(table, visited, i, j, 1, coords);
                    
                    List<int[]> made = normal(coords);      // (0, 0) 기준 정규화 : 0도
                    tableCoords.add(made);
                }
            }
        }
        
        // board에서 빈칸 덩어리를 찾아서 (0, 0) 기준 정규화를 하고
        // 각 덩어리를 tableCoords 각 원소 하나마다 90도씩 회전해서 비교
        visited = new boolean[N][N];
        boolean[] used = new boolean[tableCoords.size()];
        
        int sum = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && board[i][j] == 0) {
                    List<int[]> coords = new ArrayList<>();
                    coords.add(new int[]{i, j});
                    
                    dfs(board, visited, i, j, 0, coords);
                    
                    List<int[]> made = normal(coords);      // (0, 0) 기준 정규화
                    
                    for (int k = 0; k < tableCoords.size(); k++) {
                        if (made.size() != tableCoords.get(k).size()) {
                            continue;
                        }
                        
                        List<int[]> rotated1 = tableCoords.get(k);
                        List<int[]> rotated2 = rotate(rotated1);
                        List<int[]> rotated3 = rotate(rotated2);
                        List<int[]> rotated4 = rotate(rotated3);
                        
                        if (!used[k]) {
                            if (allMatch(made, rotated1)
                               || allMatch(made, rotated2)
                               || allMatch(made, rotated3)
                               || allMatch(made, rotated4)
                            ) {
                                used[k] = true;
                                sum += made.size();
                                break;
                            }
                        }
                    }
                }
            }
        }

        return sum;
    }
    
    public boolean allMatch(List<int[]> a, List<int[]> b) {
        for (int i = 0; i < a.size(); i++) {
            if (!(a.get(i)[0] == b.get(i)[0] && a.get(i)[1] == b.get(i)[1])) {
                return false;
            }
        }
        return true;
    }
    
    public void dfs(int[][] grid, boolean[][] visited, int x, int y, int num, List<int[]> coords) {
        visited[x][y] = true;
        
        for (int d = 0; d < 4; d++) {
            int nx = x+dx[d];
            int ny = y+dy[d];
            if (inRange(nx, ny) && !visited[nx][ny] && grid[nx][ny] == num) {
                coords.add(new int[]{nx, ny});
                dfs(grid, visited, nx, ny, num, coords);
            }
        }
    }
    
    public boolean inRange(int x, int y) {
        return (0 <= x && x < N) && (0 <= y && y < N);
    }
    
    public List<int[]> rotate(List<int[]> coords) {
        List<int[]> made = new ArrayList<>();
        for (int[] ints : coords) {
            int x = ints[0];
            int y = ints[1];
            // y, -x
            made.add(new int[]{y, -x});
        }
        // 최소 행, 최소 열 구해서 각 좌표마다 빼주기
        return normal(made);
    }
    
    public List<int[]> normal(List<int[]> lst) {
        int minRow = 50;
        int minCol = 50;
        for (int[] ints : lst) {
            minRow = Math.min(minRow, ints[0]);
            minCol = Math.min(minCol, ints[1]);
        }
        
        for (int[] ints : lst) {
            ints[0] -= minRow;
            ints[1] -= minCol;
        }
        
        lst.sort((a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
        });
        return lst;
    }
}

