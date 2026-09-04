import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        int min = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[min]) {
                min = i;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            if (i == min) {
                continue;
            }
            answer.add(arr[i]);
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        }
        return answer.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}