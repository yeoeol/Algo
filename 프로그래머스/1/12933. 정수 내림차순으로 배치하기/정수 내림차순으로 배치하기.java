import java.util.*;

class Solution {
    public long solution(long n) {
        String str = String.valueOf(n);
        String[] split = str.split("");
        List<String> arr = Arrays.stream(split)
            .sorted(Collections.reverseOrder())
            .toList();
        return Long.valueOf(String.join("", arr));
    }
}