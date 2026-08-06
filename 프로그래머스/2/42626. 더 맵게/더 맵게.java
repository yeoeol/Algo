import java.util.*;


class Solution {
    public int solution(int[] sv, int k) {
        int answer = 0;
        
        // sv 배열에서 가장 작은 두 수를 뽑아서 새로운 지수를 만들고 다시 넣기
        // 가장 작은 수가 K 이상이라면 종료
        Queue<Integer> hq = new PriorityQueue<>();
        Arrays.stream(sv).forEach(e -> hq.offer(e));
        
        while (hq.size() >= 2) {
            int p1 = hq.poll();
            int p2 = hq.poll();
            
            if (p1 >= k) {
                break;
            }
            hq.offer(p1 + (p2*2));
            answer++;
        }
        if (!hq.isEmpty()) {
            int p = hq.poll();
            if (p < k) {
                return -1;
            }
        }
        
        return answer;
    }
}