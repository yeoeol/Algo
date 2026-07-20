import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long left = 1L;
        long right = (long) n * times[times.length-1];    // 10억
        
        while (left <= right) {
            long mid = (left+right) / 2;
            
            if (can(n, times, mid)) {
                right = mid-1;
            }
            else {
                left = mid+1;
            }
        }
        
        return left;
    }
    
    public boolean can(int n, int[] times, long time) {
        // time분 내로 n명의 사람을 전부 심사할 수 있는가
        long cnt = 0;
        for (int t : times) {
            cnt += (time / t);
            if (cnt >= n) {
                return true;
            }
        }
        
        return false;
    }
}