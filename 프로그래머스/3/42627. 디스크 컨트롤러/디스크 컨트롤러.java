import java.util.*;


class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        // 대기 큐 : (작업 번호, 요청 시각, 소요 시간)
        // 소요 시간 짧은 것, 요청 시각 빠른 것, 번호가 작은 것 순으로 우선순위가 높다
        // 인터럽트 X -> 비선점
        Queue<Node> hq = new PriorityQueue<>();
        Queue<Node> cand = new PriorityQueue<>();
        for (int i = 0; i < jobs.length; i++) {
            int[] job = jobs[i];
            hq.offer(new Node(i+1, job[0], job[1]));
        }
        int t = 0;
        while (!hq.isEmpty()) {
            for (Node node : hq) {
                if (node.req <= t) {
                    cand.offer(node);
                }
            }
            if (cand.isEmpty()) {
                t += 1;
                continue;
            }
            Node p = cand.poll();
            hq.remove(p);
            
            t += p.cost;
            answer += (t - p.req);
            cand.clear();
        }
        
        return answer / jobs.length;
    }
    
    static class Node implements Comparable<Node> {
        int num;
        int req;
        int cost;
        
        public Node(int num, int req, int cost) {
            this.num = num;
            this.req = req;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Node node) {
            if (cost == node.cost) {
                if (req == node.req) {
                    return Integer.compare(num, node.num);
                }
                return Integer.compare(req, node.req);
            }
            return Integer.compare(cost, node.cost);
        }
        
        @Override
        public String toString() {
            return "num="+num
                + "|req="+req
                + "|cost="+cost;
        }
    }
}