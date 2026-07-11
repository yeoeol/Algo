import java.util.*;


class Solution {
    
    static class WordCnt {
        String word;
        int cnt;
        
        public WordCnt(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        Set<String> visited = new HashSet<>();
        
        Queue<WordCnt> queue = new LinkedList<>();
        queue.offer(new WordCnt(begin, 0));
        visited.add(begin);
        
        while (!queue.isEmpty()) {
            WordCnt wordCnt = queue.poll();
            
            String word = wordCnt.word;
            int cnt = wordCnt.cnt;
            
            if (word.equals(target)) {
                return cnt;
            }
            
            for (int i = 0; i < words.length; i++) {
                String w = words[i];
                
                if (check(word, w) && !visited.contains(w)) {
                    queue.offer(new WordCnt(w, cnt+1));
                    visited.add(w);
                }
            }
        }
        
        return 0;
    }
    
    public boolean check(String s1, String s2) {
        int n = s1.length();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                cnt++;
                if (cnt >= 2) {
                    return false;
                }
            }
        }
        return true;
    }
}