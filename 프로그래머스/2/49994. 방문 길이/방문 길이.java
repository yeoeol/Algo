import java.util.*;

class Solution {
	static int[] dxs = {0, -1, 1, 0};
	static int[] dys = {1, 0, 0, -1};

	static Map<String, Integer> map = Map.of(
			"U", 0,
			"L", 1,
			"R", 2,
			"D", 3
	);

	public int solution(String dirs) {
		int answer = 0;
		Set<String> visited = new HashSet<>();

		int x = 0, y = 0;
		for (String dir : dirs.split("")) {
			int d = map.get(dir);

			int nx = x+dxs[d], ny = y+dys[d];
			if (!inRange(nx, ny)) {
				continue;
			}
			
			String path = x + "," + y + "->" + nx + "," + ny;
			String revPath = nx + "," + ny + "->" + x + "," + y;
			
			if (!visited.contains(path)) {
				visited.add(path);
				visited.add(revPath);
				answer++;
			}
			x = nx;
			y = ny;
		}

		return answer;
	}

	public boolean inRange(int x, int y) {
		return -5 <= x && x <= 5 
			&& -5 <= y && y <= 5;
	}
}
