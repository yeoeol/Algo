import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int maxValue = nums.length / 2;
        if (set.size() < maxValue) {
            return set.size();
        }
        return maxValue;
    }
}