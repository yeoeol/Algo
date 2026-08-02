import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        int[][] grid = new int[n+1][n+1];
        
        for (int i = 0; i < results.length; i++) {
            int[] lst = results[i];
            grid[lst[0]][lst[1]] = 1;
            grid[lst[1]][lst[0]] = 2;
        }
        
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (grid[i][k] == 1 && grid[k][j] == 1) {
                        grid[i][j] = 1;
                        grid[j][i] = 2;
                    }
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            int count = 0;
            
            for (int j = 1; j <= n; j++) {
                if (i != j && grid[i][j] != 0) {
                    count++;
                }
            }
            if (count == n-1) {
                answer++;
            }
        }
        
        return answer;
    }
}