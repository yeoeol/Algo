import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        
        Set<Integer> answer = new HashSet<>();
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                answer.add(numbers[i] + numbers[j]);
            }
        }
        
        return answer.stream()
            .mapToInt(i -> i)
            .sorted()
            .toArray();
    }
}