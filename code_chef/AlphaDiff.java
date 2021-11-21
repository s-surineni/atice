import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

// https://www.codechef.com/NIUM2101/problems/ALPDIFF
class AlphaDiff {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < tc; i++) {
            String st1 = sc.nextLine();
            Set<Character> st1Set = new HashSet();
            Arrays.asList(st1.toCharArray());
            st1Set.addAll();

            String st2 = sc.nextLine();
            Set<Character> st2Set = new HashSet();
            st2Set.addAll(Arrays.asList(st2.toCharArray()));
            st2Set.removeAll(st1Set);
            String res = "";
            for (Character ch : st2Set) {
                res += String.valueOf(ch);
            }
            System.out.println(res);
        }
    }
}