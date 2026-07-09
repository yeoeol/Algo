import java.util.*;

class Solution {
    
    static Set<Integer> result = new HashSet<>();
    
    public int solution(String numbers) {
        int answer = 0;
        String[] split = numbers.split("");
        
        // 조합 만들고 각 수를 소수인지 판단
        boolean[] visited = new boolean[split.length];
        for (int i = 1; i <= split.length; i++) {
            visited = new boolean[split.length];
            per(split, i, visited, "");
        }
        
        for (int num : result) {
            if (num > 1 && isPrime(num)) {
                answer++;
            }
        }
        
        return answer;
    }
    
    public void per(String[] arr, int len, boolean[] visited, String s) {
        if (s.length() == len) {
            result.add(Integer.valueOf(s));
            return;
        }
        
        for (int i = 0; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                
                per(arr, len, visited, s + arr[i]);
                
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int num) {
        int cnt = 0;
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}