import java.util.*;


class Solution {
    
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    static int n;
    static int m;
    
    public int solution(int[][] maps) {
        int answer = 0;
        n = maps.length;
        m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        
        queue.offer(new int[]{0, 0, 1});
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            int x = p[0], y = p[1];
            int cnt = p[2];
            
            for (int i = 0; i < 4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                
                if (nx == (n-1) && ny == (m-1)) {
                    return cnt+1;
                }
                
                if (inRange(nx, ny) && maps[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, cnt+1});
                }
            }
        }
        
        return -1;
    }
    
    public boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}