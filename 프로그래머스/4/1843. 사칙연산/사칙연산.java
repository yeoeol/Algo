import java.util.*;

class Solution {
    
    public int solution(String arr[]) {
        int numberCnt = (arr.length + 1) / 2;
        
        int[][] maxDp = new int[numberCnt][numberCnt];
        int[][] minDp = new int[numberCnt][numberCnt];
        
        for (int i = 0; i < numberCnt; i++) {
            int number = Integer.parseInt(arr[i * 2]);
            
            maxDp[i][i] = number;
            minDp[i][i] = number;
        }
        
        // 구간 길이
        for (int len = 2; len <= numberCnt; len++) {
            for (int left = 0; left + len - 1 < numberCnt; left++) {
                int right = left + len - 1;
                
                maxDp[left][right] = Integer.MIN_VALUE;
                minDp[left][right] = Integer.MAX_VALUE;
                
                for (int sp = left; sp < right; sp++) {
                    String operator = arr[sp * 2 + 1];
                    if (operator.equals("+")) {
                        maxDp[left][right] = Math.max(maxDp[left][right], maxDp[left][sp] + maxDp[sp+1][right]);
                        minDp[left][right] = Math.min(minDp[left][right], minDp[left][sp] + minDp[sp+1][right]);
                    }
                    else {
                        maxDp[left][right] = Math.max(maxDp[left][right], maxDp[left][sp] - minDp[sp+1][right]);
                        minDp[left][right] = Math.min(minDp[left][right], minDp[left][sp] - maxDp[sp+1][right]);
                    }
                }
            }
        }
        
        return maxDp[0][numberCnt-1];
    }
}