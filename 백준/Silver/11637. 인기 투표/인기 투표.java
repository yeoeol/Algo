import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int count = Integer.parseInt(br.readLine());

            Map<Integer, Integer> map = new HashMap<>();
            int maxVote = 0;

            // 가장 큰 투표 수 구하기
            int totalVotes = 0;
            for (int i = 1; i <= count; i++) {
                int vote = Integer.parseInt(br.readLine());
                if (vote > maxVote) {
                    maxVote = vote;
                }
                totalVotes += vote;
                map.put(i, vote);
            }

            // 가장 큰 투표 수와 같은 사람 구하기
            List<Integer> answer = new ArrayList<>();
            int finalMaxVote = maxVote;
            map.forEach((key, value) -> {
                if (value == finalMaxVote) {
                    answer.add(key);
                }
            });

            int half = totalVotes/2 + 1;
            if (answer.size() == 1 && maxVote >= half) {
                System.out.println("majority winner " + answer.get(0));
            } else if (answer.size() == 1) {
                System.out.println("minority winner " + answer.get(0));
            } else {
                System.out.println("no winner");
            }
        }
    }
}