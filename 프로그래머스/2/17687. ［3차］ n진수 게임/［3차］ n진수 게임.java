class Solution {

	static String numbers = "0123456789ABCDEF";

	public String solution(int n, int t, int m, int p) {
		// 0, 1, 1, 0, 1, 1, 1, 0, 0 => 0, 1, 1, 1
		// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 1, 1, 1, ...
		// 17 => 0001 0001

		// 사용할 진법의 수 (2진수면 0, 1), (16진수면 0, 1, ..., A, B, ..., F)

		String result = " ";
		// 구해야 하는 문자열의 길이
		int length = t * m + p;
		for (int i = 0; i <= length; i++) {
			result += trans(n, i);
			if (result.length() >= length) {
				break;
			}
		}
        
        String answer = "";
        for (int i = p; i < length; i += m) {
            answer += result.charAt(i);
        }

		return answer;
	}

	// 10진수 decimal을 n진법 수로 변환하는 함수
	public String trans(int n, int decimal) {
		if (decimal == 0) {
			return "0";
		}
		String sets = numbers.substring(0, n);
		String result = "";
		while (decimal != 0) {
			int temp = decimal % n;
			result = sets.charAt(temp) + result;
			decimal /= n;
		}
		return result;
	}
}
