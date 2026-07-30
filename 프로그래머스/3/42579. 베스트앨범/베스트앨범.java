import java.util.*;

class Solution {
	public int[] solution(String[] genres, int[] plays) {
		List<Integer> answer = new ArrayList<>();
		int n = genres.length;

		// 장르별 총 재생 횟수
		Map<String, Integer> p = new HashMap<>();
		for (int i = 0; i < n; i++) {
			String key = genres[i];
			if (p.containsKey(key)) {
				p.put(key, p.get(key) + plays[i]);
			} else {
				p.put(key, plays[i]);
			}
		}

		// 장르별 고유 번호
		Map<String, List<Integer>> g = new HashMap<>();
		for (int i = 0; i < n; i++) {
			String key = genres[i];
			if (g.containsKey(key)) {
				List<Integer> lst = g.get(key);
				lst.add(i);
			} else {
				List<Integer> lst = new ArrayList<>();
				lst.add(i);
				g.put(key, lst);
			}
		}

		Comparator<Integer> c = (a, b) -> {
			if (plays[a] != plays[b]) {
                return Integer.compare(plays[b], plays[a]);
            }
			return Integer.compare(a, b);
		};

        List<String> genreOrder = new ArrayList<>(p.keySet());
        genreOrder.sort((a, b) -> Integer.compare(p.get(b), p.get(a)));
        
		List<Integer> lst = p.values().stream().sorted(Comparator.reverseOrder()).toList();
		int idx = 0;
		for (String key : genreOrder) {
			if (p.get(key).equals(lst.get(idx))) {
				idx++;

				List<Integer> l = g.get(key);
				l.sort(c);
                for (int i = 0; i < Math.min(l.size(), 2); i++) {
                    answer.add(l.get(i));
                }
			}
		}
        
		return answer.stream().mapToInt(Integer::intValue).toArray();
	}
}