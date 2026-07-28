import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, List<String>> map = new HashMap<>();
        for (String[] cloth : clothes) {
            if (!map.keySet().contains(cloth[1])) {
                List<String> temp = new ArrayList<>();
                temp.add(cloth[0]);
                map.put(cloth[1], temp);
                continue;
            }
            
            List<String> result = map.get(cloth[1]);
            result.add(cloth[0]);
        }
        
        List<Integer> lst = new ArrayList<>();
        for (String key : map.keySet()) {
            answer *= (map.get(key).size() + 1);
        }
        
        return answer-1;
    }
}