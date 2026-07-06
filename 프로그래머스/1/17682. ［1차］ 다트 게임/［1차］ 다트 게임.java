import java.util.*;

class Solution {

    static Map<Character, Integer> powerMap = Map.of('S', 1, 'D', 2, 'T', 3);

	int n;

	public int solution(String dart) {
		n = dart.length();

		List<Integer> results = new ArrayList<>();

		int i = 0;
		while (i < n) {
			int score = 0;

			// 숫자 파싱
			if (i + 1 < n && dart.charAt(i) == '1' && dart.charAt(i + 1) == '0') {
				score = 10;
				i += 2;
			} else {
				score = dart.charAt(i) - '0';
				i += 1;
			}

			// 보너스
			char bonus = dart.charAt(i);
			score = (int) Math.pow(score, powerMap.get(bonus));
			i++;

			// 옵션
			if (i < n) {
				char option = dart.charAt(i);
				if (option == '*' || option == '#') {
					if (option == '*') {
						score *= 2;
						if (!results.isEmpty()) {
							int lastScore = results.getLast()*2;
							results.set(results.size()-1, lastScore);
						}
					} else {
						score *= -1;
					}
					i++;
				}
			}

			results.add(score);
		}

		return results.stream()
				.mapToInt(Integer::intValue)
				.sum();
	}
}