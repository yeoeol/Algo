import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, numbers[0]});
        queue.add(new int[]{0, -numbers[0]});
        
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            int idx = p[0], sum = p[1];
            
            if (sum == target && (idx == numbers.length-1)) {
                answer++;
                continue;
            }
            
            if (idx == numbers.length-1) {
                continue;
            }
            
            queue.add(new int[]{idx+1, sum+numbers[idx+1]});
            queue.add(new int[]{idx+1, sum-numbers[idx+1]});
        }
        
        return answer;
    }
}