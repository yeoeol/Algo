import java.util.*;

class Solution {
    public boolean solution(String[] pb) {
        boolean answer = true;
        Arrays.sort(pb);
        
        for (int i = 0; i < pb.length-1; i++) {
            if (startswith(pb[i], pb[i+1])) {
                answer = false;
                break;
            }
        }
        
        return answer;
    }
    
    public boolean startswith(String s1, String s2) {
        for (int i = 0; i < Math.min(s1.length(), s2.length()); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}