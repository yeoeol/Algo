import java.util.*;

class Solution {
    static List<String> result = new ArrayList<>();
    
    public int solution(String word) {
        // A, E, I, O, U 로 1부터 5까지의 r을 조합
        // 정렬 후 word의 index + 1
        String[] arr = new String[]{"A", "E", "I", "O", "U"};
        
        for (int r = 1; r <= 5; r++) {
            per(arr, 5, r, "");
        }
        
        result = result.stream()
            .sorted()
            .toList();
        
        return result.indexOf(word) + 1;
    }
    
    public void per(String[] arr, int n, int r, String s) {
        if (s.length() == r) {
            result.add(s);
            return;
        }
        
        for (int i = 0; i < arr.length; i++) {
            per(arr, n, r, s+arr[i]);
        }
    }
}