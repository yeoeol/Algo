import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String a = sc.next();
        String answer = "";
        for (int i = 0; i < a.length(); i++) {
            if (isUpper(a.charAt(i))) {
                System.out.print((char) (a.charAt(i) - 'A' + 'a'));
            }
            else {
                System.out.print((char) (a.charAt(i) - 'a' + 'A'));
            }
        }
    }
    
    public static boolean isUpper(char c) {
        if ('A' <= c && c <= 'Z') {
            return true;
        }
        return false;
    }
}