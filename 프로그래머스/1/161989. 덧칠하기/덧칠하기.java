class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int i = 0;
        while (i < section.length) {
            answer++;
            int start = section[i];
            int end = start + m - 1;
            while (i < section.length && start <= section[i] && section[i] <= end) {
                i++;
            }
        }
        return answer;
    }
}