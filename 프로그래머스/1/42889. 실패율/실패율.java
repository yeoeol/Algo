import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        List<Integer> answer = new ArrayList<>();
        int[] count = new int[N+2];
        
        for (int stage : stages) {
            count[stage]++;
        }
        
        int init = stages.length;
        
        Map<Double, List<Integer>> map = new HashMap<>();
        for (int i = 1; i < count.length-1; i++) {
            if (count[i] == 0) {
                if (map.containsKey(0.0)) {
                    map.get(0.0).add(i);
                }
                else {
                    List<Integer> arr = new ArrayList<>();
                    arr.add(i);
                    map.put(0.0, arr);
                }
                continue;
            }
            double key = count[i]/(double)init;
            init -= count[i];
            
            if (map.containsKey(key)) {
                map.get(key).add(i);
            }
            else {
                List<Integer> arr = new ArrayList<>();
                arr.add(i);
                map.put(key, arr);
            }
        }
        System.out.println(map);
        
        List<Double> keys = map.keySet().stream()
            .sorted(Collections.reverseOrder())
            .toList();
        
        for (Double key : keys) {
            List<Integer> arr = map.get(key);
            for (int i = 0; i < arr.size(); i++) {
                answer.add(arr.get(i));
            }
        }
        
        return answer.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}