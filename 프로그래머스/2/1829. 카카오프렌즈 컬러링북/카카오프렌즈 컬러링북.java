class Solution {
    
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int r;
    static int c;
    
    public int[] solution(int m, int n, int[][] picture) {
        r = m; c = n;
        int[] answer = new int[2];
        
        int areaCnt = 0;
        int area = 0;
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] == 0 || visited[i][j]) {
                    continue;
                }
                areaCnt++;
                area = Math.max(area, dfs(picture, i, j, picture[i][j], visited));
            }
        }
        
        return new int[]{areaCnt, area};
    }
    
    public int dfs(int[][] grid, int x, int y, int value, boolean[][] visited) {
        int cnt = 1;
        visited[x][y] = true;
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (inRange(nx, ny) && !visited[nx][ny] && grid[nx][ny] == value) {
                cnt += dfs(grid, nx, ny, value, visited);
            }
        }
        return cnt;
    }
    
    public boolean inRange(int x, int y) {
        return 0 <= x && x < r && 0 <= y && y < c;
    }
}