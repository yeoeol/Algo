import java.util.*;

class Solution {

	private final List<List<Integer>> combinations = new ArrayList<>();
	private final List<Set<Integer>> candidateKeys = new ArrayList<>();

	public int solution(String[][] relation) {
		int columnCount = relation[0].length;

		for (int size = 1; size <= columnCount; size++) {
			combinations.clear();
			combination(0, columnCount, size, new ArrayList<>());

			for (List<Integer> cols : combinations) {
				if (!isMinimal(cols)) {
					continue;
				}
				if (isUnique(relation, cols)) {
					candidateKeys.add(new HashSet<>(cols));
				}
			}
			combinations.clear();
		}


		return candidateKeys.size();
	}

	private boolean isUnique(String[][] relation, List<Integer> cols) {
		Set<List<String>> set = new HashSet<>();

		for (String[] row : relation) {
			List<String> values = new ArrayList<>();

			for (Integer col : cols) {
				values.add(row[col]);
			}
			set.add(values);
		}
		return set.size() == relation.length;
	}

	private boolean isMinimal(List<Integer> cols) {
		Set<Integer> current = new HashSet<>(cols);
		for (Set<Integer> candidateKey : candidateKeys) {
			if (current.containsAll(candidateKey)) {
				return false;
			}
		}
		return true;
	}

	private void combination(int start, int n, int count, List<Integer> selected) {
		if (selected.size() == count) {
			combinations.add(new ArrayList<>(selected));
			return;
		}

		for (int i = start; i < n; i++) {
			selected.add(i);
			combination(i+1, n, count, selected);
			selected.removeLast();
		}
	}
}