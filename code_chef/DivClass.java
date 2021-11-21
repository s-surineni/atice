import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class DivClass {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner in = new Scanner(System.in);
        int tc = Integer.parseInt(in.nextLine());
        // System.out.println(tc);
        for (int i = 0; i < tc; i++) {
            // int valLen = in.nextInt();
            int valLen = Integer.parseInt(in.nextLine());
            if (valLen < 12) {
                in.nextLine();
                System.out.println("no");
                continue;
            }
            // in.nextLine();
            String[] students = in.nextLine().split(" ");
            // String[] students = "1 2 3".split(" ");

            int[] studentHeight = new int[valLen];
            Set<Integer> heights = new HashSet<>();
            for (int idx2 = 0; idx2 < valLen; idx2++) {
                studentHeight[idx2] = Integer.parseInt(students[idx2]);
                heights.add(Integer.parseInt(students[idx2]));
            }
            if (heights.size() > 12) {
                System.out.println("no");
            } else {
                System.out.println("yes");
            }
        }
    }
}