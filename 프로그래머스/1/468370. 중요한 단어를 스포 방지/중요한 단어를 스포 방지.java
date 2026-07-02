import java.util.*;

class Solution {
	public int solution(String message, int[][] spoiler_ranges) {
		String[] split = message.split(" ");
        int n = split.length;
        
        List<int[]> maps = new ArrayList<>();
        int start = 0;
        int end = 0;
        for (String s : split) {
            end = start + s.length();
            int[] range = new int[]{start, end-1};
            maps.add(range);
            
            start = end+1;
        }
        
        boolean[] spo = new boolean[n];
        for (int i = 0; i < spoiler_ranges.length; i++) {
            int a = spoiler_ranges[i][0];
            int b = spoiler_ranges[i][1];
            for (int j = 0; j < n; j++) {
                int wordStart = maps.get(j)[0];
                int wordEnd = maps.get(j)[1];
                
                if (!(wordEnd < a || wordStart > b)) {
                    spo[j] = true;
                }
            }
        }
        
        Set<String> nonSpoilerWords = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (!spo[i]) {
                nonSpoilerWords.add(split[i]);
            }
        }
        
        Set<String> processedSpoilerWords = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            if (!spo[i]) {
                continue;
            }
            
            String word = split[i];
            // 스포일러가 아닌 일반 구간에 등장한 적이 없어야 함
            // 이전에 스포일러 해제로 공개된 적이 없어야 함
            if (!nonSpoilerWords.contains(word) && 
               !processedSpoilerWords.contains(word)) {
                processedSpoilerWords.add(word);
            }
        }

		return processedSpoilerWords.size();
	}
}