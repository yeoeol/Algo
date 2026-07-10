import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100;
        boolean[] visited = new boolean[n+1];
        List<Integer> nodes = new ArrayList<>();
        
        // 트리 1개를 2개로 분할하는데, 2개의 트리 노드 수 차이 최솟값이 되는 간선 끊기
        // 간선을 하나씩 다 끊어보고, 나누어진 2개의 트리를 대상으로 dfs를 돌려서 노드의 수를 세기
        int[][] grid = new int[n+1][n+1];   // 1-based
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0], b = wires[i][1];
            grid[a][b] = 1;
            grid[b][a] = 1;
        }
        
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0], b = wires[i][1];
            
            visited = new boolean[n+1];
            nodes.clear();
            
            grid[a][b] = 0;
            grid[b][a] = 0;
            
            for (int node = 1; node <= n; node++) {
                if (!visited[node]) {
                    int nodeCnt = dfs(grid, node, visited);
                    nodes.add(nodeCnt);
                }
            }
            
            int diff = Math.abs(nodes.get(0) - nodes.get(1));
            answer = Math.min(answer, diff);
            
            grid[a][b] = 1;
            grid[b][a] = 1;
        }
        
        return answer;
    }
    
    public int dfs(int[][] grid, int start, boolean[] visited) {
        visited[start] = true;
        int cnt = 1;
        
        for (int y = 1; y < grid.length; y++) {
            if (grid[start][y] == 1 && !visited[y]) {
                cnt += dfs(grid, y, visited);
            }
        }
        return cnt;
    }
}