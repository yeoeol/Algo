import java.util.*;

class Solution {

	static List<String> arr = List.of(
			"A", "C", "F", "J", "M", "N", "R", "T"
	);
	static List<List<String>> cs = new ArrayList<>();

	public int solution(int n, String[] data) {
        cs = new ArrayList<>();
		int answer = 0;

		comb(new ArrayList<>());

		boolean flag;
		for (List<String> lst : cs) {
			flag = true;
			for (String d : data) {
				String a = String.valueOf(d.charAt(0));
				String b = String.valueOf(d.charAt(2));
				String op = String.valueOf(d.charAt(3));
				String interval = String.valueOf(d.charAt(4));
				if (!check(lst, a, b, op, interval)) {
					flag = false;
					break;
				}
			}
			if (flag) {
				answer++;
			}
		}
		return answer;
	}

	public void comb(List<String> combinations) {
		if (combinations.size() == arr.size()) {
			cs.add(List.copyOf(combinations));
			return;
		}
		for (int i = 0; i < arr.size(); i++) {
			if (combinations.contains(arr.get(i))) {
				continue;
			}
			combinations.add(arr.get(i));
			comb(combinations);
			combinations.removeLast();
		}
	}

	public boolean check(List<String> arr, String a, String b, String op, String interval) {
		int inter = Math.abs(arr.indexOf(a) - arr.indexOf(b)) - 1;
		int value = Integer.parseInt(interval);
		if ("=".equals(op)) {
			return inter == value;
		} else if ("<".equals(op)) {
			return inter < value;
		} else {
			return inter > value;
		}
	}
}