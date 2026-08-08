import java.util.*;

class Solution {
    
    Queue<Integer> maxHq = new PriorityQueue<>();
    Queue<Integer> minHq = new PriorityQueue<>();
    
    public int[] solution(String[] operations) {
        for (String op : operations) {
            String[] split = op.split(" ");
            String o = split[0];
            int num = Integer.valueOf(split[1]);
            
            order(o, num);
        }
        
        if (maxHq.isEmpty() || minHq.isEmpty()) {
            return new int[]{0, 0};
        }
        
        int M = -maxHq.poll();
        int m = minHq.poll();
        return new int[]{M, m};
    }
    
    public void order(String op, int num) {
        if (op.equals("I")) {
            maxHq.offer(-num);
            minHq.offer(num);
            return;
        }
        if (maxHq.isEmpty() || minHq.isEmpty()) {
            return;
        }
        
        if (op.equals("D") && num == 1) {
            int v = -maxHq.poll();
            minHq.remove(v);
        }
        else {
            int v = minHq.poll();
            maxHq.remove(-v);
        }
    }
}