class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        // brown + yellow를 두 수의 곱으로 나눈 모든 경우의 수를 구하고
        // 두 수의 차이가 가장 작은 것이 답

        int n = (brown-4) / 2;
        for (int i = 1; i <= n/2; i++) {
            if (i * (n-i) == yellow) {
                int max = Math.max(i, n-i);
                int min = Math.min(i, n-i);
                answer[0] = max+2;
                answer[1] = min+2;
            }
        }
        
        return answer;
    }
}