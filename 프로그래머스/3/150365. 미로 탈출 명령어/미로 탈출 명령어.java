import java.util.*;

class Solution {
    
    static int[] dxs = {-1, 0, 1, 0};
    static int[] dys = {0, 1, 0, -1};
    
    static String[] map = {"u", "r", "d", "l"};
    
    static int N;
    static int M;
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        String answer = "";
        N = n; 
        M = m;
        
        answer = bfs(x, y, r, c, k);
        return answer;
    }
    
    public String bfs(int x, int y, int r, int c, int k) {
        Queue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(x, y, ""));
        
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            
            int mStep = k - cur.path.length(); // 목적지까지 남은 최소 거리
            int mDist = Math.abs(r - cur.x) + Math.abs(c - cur.y);
            
            if (mStep % 2 != mDist % 2) {
                continue;
            }
            if (mStep < mDist) {
                continue;
            }
            
            if (cur.x == r && cur.y == c && cur.path.length() == k) {
                return cur.path;
            }
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dxs[i];
                int ny = cur.y + dys[i];
                if (inRange(nx, ny)) {
                    pq.offer(new Node(nx, ny, cur.path + map[i]));
                }
            }
        }
        return "impossible";
    }
    
    public boolean inRange(int x, int y) {
        return 1 <= x && x <= N && 1 <= y && y <= M;
    }
    
    static class Node implements Comparable<Node> {
        int x, y;
        String path;
        
        public Node(int x, int y, String path) {
            this.x = x;
            this.y = y;
            this.path = path;
        }
        
        @Override
        public int compareTo(Node node) {
            return this.path.compareTo(node.path);
        }
    }
}