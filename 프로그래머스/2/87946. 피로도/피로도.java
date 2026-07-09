import java.util.*;


class Solution {
    
    static List<List<Integer>> result = new ArrayList<>();
    
    public int solution(int k, int[][] ds) {
        int answer = -1;
        int n = ds.length;
        
        int[] arr = new int[n];
        List<Integer> res = new ArrayList<>();
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = i;
        }
        
        per(arr, n, n, res, visited);
        
        for (List<Integer> lst : result) {
            int cnt = explore(k, lst, ds);
            answer = Math.max(answer, cnt);
        }
        
        return answer;
    }
    
    public void per(int[] arr, int n, int r, List<Integer> res, boolean[] visited) {
        if (res.size() == r) {
            result.add(new ArrayList<>(res));
            return;
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                res.add(i);
                per(arr, n, r, res, visited);
                res.removeLast();
                visited[i] = false;
            }
        }
    }
    
    public int explore(int cur, List<Integer> orders, int[][] ds) {
        int cnt = 0;
        
        for (int idx : orders) {
            int minNeed = ds[idx][0];
            int use = ds[idx][1];
            
            if (cur >= minNeed) {
                cnt++;
                cur -= use;
            }
            else {
                return cnt;
            }
        }
        return cnt;
    }
}