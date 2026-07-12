import java.util.*;

class Solution {
    static int[][] grid;
    static final int INHIBIT = -1;
    static final int N = 110;
    
    static int[] dx = new int[]{-1, 1, 0, 0};
    static int[] dy = new int[]{0, 0, -1, 1};
    
    public int solution(int[][] rectangle, int cx, int cy, int itemX, int itemY) {
        grid = new int[N][N];
        
        for (int[] r : rectangle) {
            for (int i = 0; i < r.length; i++) {
                r[i] *= 2;
            }
        }
        
        for (int i = 1; i <= rectangle.length; i++) {
            int[] coords = rectangle[i-1];
            
            int x1 = coords[0], y1 = coords[1];
            int x2 = coords[2], y2 = coords[3];
            
            for (int x = x1; x <= x2; x++) {
                if (grid[x][y1] != INHIBIT) {
                    grid[x][y1] = 1;
                }
                if (grid[x][y2] != INHIBIT) {
                    grid[x][y2] = 1;
                }
            }
            
            for (int y = y1; y <= y2; y++) {
                if (grid[x1][y] != INHIBIT) {
                    grid[x1][y] = 1;
                }
                if (grid[x2][y] != INHIBIT) {
                    grid[x2][y] = 1;
                }
            }
            
            for (int x = x1+1; x < x2; x++) {
                for (int y = y1+1; y < y2; y++) {
                    grid[x][y] = INHIBIT;
                }
            }
        }
        
        return bfs(cx*2, cy*2, itemX*2, itemY*2) / 2;
    }
    
    public int bfs(int cx, int cy, int itemX, int itemY) {
        boolean[][] visited = new boolean[N][N];
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{cx, cy, 0});
        
        visited[cx][cy] = true;
        
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            int x = p[0], y = p[1], cnt = p[2];
            if (x == itemX && y == itemY) {
                return cnt;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                
                if (grid[nx][ny] != 0 && 
                    grid[nx][ny] != INHIBIT && 
                    !visited[nx][ny]) {
                    
                    queue.offer(new int[]{nx, ny, cnt+1});
                    visited[nx][ny] = true;
                }
            }
        }
        return 1;
    }
}