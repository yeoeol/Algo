class Solution {
    public int solution(int[][] sizes) {
        int n = sizes.length;
        int m = sizes[0].length;
        
        int garo = 0;   // 가로 길이 최대
        int sero = 0;   // 세로 길이 최대
        for (int i = 0; i < n; i++) {
            int g = sizes[i][0];
            int s = sizes[i][1];
            if (g > s) {
                garo = Math.max(garo, s);
                sero = Math.max(sero, g);
            }
            else {
                garo = Math.max(garo, g);
                sero = Math.max(sero, s);
            }
        }
        return garo * sero;
    }
}
