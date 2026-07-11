class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(computers, i, visited);
                answer++;
            }
        }
        
        return answer;
    }
    
    public void dfs(int[][] grid, int start, boolean[] visited) {
        visited[start] = true;
        
        int[] nxts = grid[start];
        for (int i = 0; i < nxts.length; i++) {
            if (!visited[i] && nxts[i] == 1) {
                dfs(grid, i, visited);
            }
        }
    }
}