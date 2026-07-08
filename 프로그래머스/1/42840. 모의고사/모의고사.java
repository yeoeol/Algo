import java.util.*;

class Solution {
    
    static int[] a = {1, 2, 3, 4, 5};
    static int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
    static int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    public int[] solution(int[] answers) {
        int[] score = new int[3];
        
        int ai = 0;
        int bi = 0;
        int ci = 0;
        
        for (int i = 0; i < answers.length; i++) {
            int num = answers[i];
            if (num == a[ai]) {
                score[0]++;
            }
            if (num == b[bi]) {
                score[1]++;
            }
            if (num == c[ci]) {
                score[2]++;
            }
            ai = (ai + 1) % a.length;
            bi = (bi + 1) % b.length;
            ci = (ci + 1) % c.length;
        }
        
        Stack<Integer> answer = new Stack<>();
        
        for (int i = 0; i < 3; i++) {
            if (answer.isEmpty()) {
                answer.push(i+1);
                continue;
            }
            
            if (score[answer.peek()-1] == score[i]) {
                answer.push(i+1);
            } else {
                if (score[answer.peek()-1]  < score[i]) {
                    while (!answer.isEmpty()) {
                        answer.pop();
                    }
                    answer.push(i+1);
                }
            }
        }
        
        return answer.stream()
                .mapToInt(v -> v)
                .toArray();
    }
}