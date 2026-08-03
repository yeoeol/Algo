import java.util.*;

class Solution {
    
    static String MSG = "";
    static Map<String, Integer> map;
    
    public int[] solution(String msg) {
        MSG = msg;
        List<Integer> answer = new ArrayList<>();
        
        // 1. 사전 초기화
        map = new HashMap<>();
        int value = 1;
        String temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < temp.length(); i++) {
            String key = String.valueOf(temp.charAt(i));
            map.put(key, value++);
        }
        
        // 2. 반복
        while (true) {
            String w = getCurInput();
            int idx = map.get(w);
            answer.add(idx);
            
            // 3.
            MSG = MSG.substring(w.length(), MSG.length());
            
            // 4.
            if (MSG.length() != 0 && !MSG.equals("")) {
                map.put(w + String.valueOf(MSG.charAt(0)), value++);
            } else {
                break;
            }
        }
        
        return answer.stream()
            .mapToInt(Integer::new)
            .toArray();
    }
    
    public static String getCurInput() {
        for (int i = 0; i < MSG.length(); i++) {
            String key = MSG.substring(0, MSG.length()-i);
            if (map.containsKey(key)) {
                return key;
            }
        }
        return String.valueOf(MSG.charAt(0));
    }
}