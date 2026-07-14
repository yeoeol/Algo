import java.util.*;

class Solution {
    
    static List<List<String>> paths = new ArrayList<>();

	public String[] solution(String[][] tickets) {
		boolean[] visited = {};
		
		for (int i = 0; i < tickets.length; i++) {
			String[] ticket = tickets[i];
			if (ticket[0].equals("ICN")) {
				visited = new boolean[tickets.length];
				
				List<String> path = new ArrayList<>();
				path.add("ICN");
                visited[i] = true;
                
				dfs(tickets, path, visited, i);
			}
		}
        
		List<String> list = paths.stream()
				.sorted((o1, o2) -> {
					for (int i = 0; i < o1.size(); i++) {
						String s1 = o1.get(i);
						String s2 = o2.get(i);
						if (s1.compareTo(s2) == 0) {
							continue;
						}
						return s1.compareTo(s2);
					}
					return 0;
				})
				.findFirst()
				.get();
        
		String[] answer = new String[list.size()];
		int i = 0;
		for (String s : list) {
			answer[i++] = s;
		}

		return answer;
	}

	public void dfs(String[][] tickets, List<String> path, boolean[] visited, int idx) {
        visited[idx] = true;
        path.add(tickets[idx][1]);
        
        if (tickets.length+1 == path.size()) {
            paths.add(new ArrayList<>(path));
        }
        else {
            for (int i = 0; i < tickets.length; i++) {
                if (!visited[i] && tickets[i][0].equals(path.getLast())) {
                    dfs(tickets, path, visited, i);
                }
            }
        }
        
        visited[idx] = false;
        path.removeLast();
	}
}