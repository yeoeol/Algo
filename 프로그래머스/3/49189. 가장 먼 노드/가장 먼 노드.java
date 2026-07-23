import java.util.*;

class Solution {
    private List<List<Integer>> grid = new ArrayList<>();
    private int maxValue = 0;
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        for (int i = 0; i < n+1; i++) {
            grid.add(new ArrayList<>());
        }
        
        for (int[] e : edge) {
            grid.get(e[0]).add(e[1]);
            grid.get(e[1]).add(e[0]);
        }
        
        int[] dist = bfs(n, 1);
        for (int i = 0; i < dist.length; i++) {
            if (dist[i] == maxValue) {
                answer++;
            }
        }
        
        return answer;
    }
    
    public int[] bfs(int n, int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        
        boolean[] visited = new boolean[n+1];
        visited[start] = true;
        
        int[] dist = new int[n+1];
        
        while (!queue.isEmpty()) {
            int p = queue.poll();
            for (int nxt : grid.get(p)) {
                if (!visited[nxt]) {
                    dist[nxt] = dist[p] + 1;
                    visited[nxt] = true;
                    
                    queue.offer(nxt);
                    maxValue = Math.max(maxValue, dist[nxt]);
                }
            }
        }
        return dist;
    }
}