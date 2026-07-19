import java.util.*;


class Solution {
    static int N;
    
    public int solution(int[] money) {
        N = money.length;
        
        // dp[i][0] : i번째 집을 훔쳤을 때
        // dp[i][1] : i번째 집을 훔치지 않았을 때
        int[][] dp = new int[N][2];  
        dp[0][0] = money[0];
        // 첫 번째 집을 먹었을 때, 마지막 집은 먹지 않음
        for (int i = 1; i < N-1; i++) {
            dp[i][0] = dp[i-1][1]+money[i];
            dp[i][1] = Math.max(dp[i-1][0], dp[i-1][1]);
        }
        
        dp[N-1][0] = Math.max(dp[N-2][0], dp[N-2][1]);
        dp[N-1][1] = Math.max(dp[N-2][0], dp[N-2][1]);
        
        int answer = Math.max(dp[N-1][0], dp[N-1][1]);
        
        dp[0][0] = 0;
        // 첫 번째 집을 먹지 않았을 때, 마지막 집은 먹음
        for (int i = 1; i < N-1; i++) {
            dp[i][0] = dp[i-1][1] + money[i];
            dp[i][1] = Math.max(dp[i-1][0], dp[i-1][1]);
        }
        
        dp[N-1][0] = dp[N-2][1] + money[N-1];
        dp[N-1][1] = Math.max(dp[N-2][0], dp[N-2][1]);
        
        answer = Math.max(answer, Math.max(dp[N-1][0], dp[N-1][1]));
        return answer;
    }
}