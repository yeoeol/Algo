import java.util.*;

class Solution {
    public String solution(String[] p, String[] c) {
        String answer = "";
        
        Arrays.sort(p);
        Arrays.sort(c);
        
        for (int i = 0; i < c.length; i++) {
            if (!p[i].equals(c[i])) {
                answer = p[i];
                break;
            }
        }
        
        return answer.equals("") ? p[p.length-1] : answer;
    }
}