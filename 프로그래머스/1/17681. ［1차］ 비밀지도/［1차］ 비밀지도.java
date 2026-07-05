class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        // arr1의 각 원소를 2진수로 변환
        String[] a1 = transform(arr1, n);
        // // arr2의 각 원소를 2진수로 변환
        String[] a2 = transform(arr2, n);
        
        // n*n 2중 for문을 돌면서 하나라도 1인 부분이 있다면 #, 아니라면 공백
        for (int i = 0; i < n; i++) {
            String result = "";
            for (int j = 0; j < n; j++) {
                if (a1[i].charAt(j) == '1' || a2[i].charAt(j) == '1') {
                    result += "#";
                } else {
                    result += " ";
                }
            }
            answer[i] = result;
        }
        return answer;
    }
    
    public String[] transform(int[] arr, int n) {
        String[] grid = new String[n];
        for (int i = 0; i < n; i++) {
            String bin = DecimalTobinary(arr[i], n);
            grid[i] = bin;
        }
        return grid;
    }
    
    public String DecimalTobinary(int dec, int n) {
        String bin = "";
        int q = dec;
        int r = 0;
        while (q != 0) {
            r = q % 2;
            q = q / 2;
            bin = r + bin;
        }
        while (bin.length() != n) {
            bin = "0" + bin;
        }
        return bin;
    }
}