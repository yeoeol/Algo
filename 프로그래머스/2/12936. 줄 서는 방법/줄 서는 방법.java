import java.util.*;

class Solution {
    
    List<Integer> arr = new ArrayList<>();
    
    public int[] solution(int n, long k) {
        k--;
        
        int[] answer = new int[n];
        int idx = 0;
        
        for (int i = 1; i <= n; i++) {
            arr.add(i);
        }
        
        while (idx < n) {
            long gap = factorial(arr.size()-1);

            long q = k / gap;
            answer[idx++] = arr.get((int)q);
            k -= gap * q;
            arr.remove((int)q);
        }
        
        return answer;
    }
    
    public long factorial(int num) {
        if (num == 0) {
            return 1;
        }
        return num * factorial(num-1);
    }
}