import java.util.*;


class Solution {
	public int solution(int N, int number) {
		List<Set<Integer>> result = new ArrayList<>();
		// 5, 55
		// N 3개를 사용한 결과 =
		// N 1개로 만든 값과 N 2개로 만든 값 사칙연산
		// N 2개로 만든 값과 N 1개로 만든 값 사칙연산
		// N을 이어붙인 NNN

		// 일반화 : N을 i번 사용한 집합 = N을 j번 사용한 집합과 N을 (i-j)번 사용한 집합을 조합

		result.add(Set.of());

		for (int i = 1; i <= 8; i++) {
			Set<Integer> sets = new HashSet<>();
			int num = getNum(N, i);
			sets.add(num);

			for (int j = 1; j < i; j++) {
				for (Integer a : result.get(j)) {
					for (Integer b : result.get(i-j)) {
						sets.addAll(make(a, b));
					}
				}
			}
			if (sets.contains(number)) {
				return i;
			}
			result.add(sets);
		}

		return -1;
	}

	public int getNum(int N, int k) {
		int n = N;
		while (--k > 0) {
			n = n*10 + N;
		}
		return n;
	}

	public Set<Integer> make(int a, int b) {
		Set<Integer> sets = new HashSet<>();
		sets.add(a+b);
		sets.add(a-b);
		sets.add(a*b);
		if (b != 0) {
			sets.add(a/b);
		}
		return sets;
	}

}