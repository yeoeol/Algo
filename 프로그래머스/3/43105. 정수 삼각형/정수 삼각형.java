import java.util.*;


class Solution {
    public int solution(int[][] triangle) {
        int[][] dp = new int[triangle.length][triangle.length];
        dp[0][0] = triangle[0][0];
        
        // n : 1..triangle.length-1
        // m : 1..n-1
        // dp[n][0] = dp[n-1][0] + triangle[n][0];
        // dp[n][m] = Math.max(dp[n-1][m-1], triangle[n-1][m]) + triangle[n][m];
        // dp[n][n] = dp[n-1][n-1] + triangle[n][n];
        
        for (int i = 1; i < triangle.length; i++) {
            dp[i][0] = dp[i-1][0] + triangle[i][0];
            for (int j = 1; j < i; j++) {
                dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            }
            dp[i][i] = dp[i-1][i-1] + triangle[i][i];
        }

        
        int[] cand = dp[dp.length-1];
        return Arrays.stream(cand).max().getAsInt();
    }
}