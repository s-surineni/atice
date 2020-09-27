import java.util.*;

class StringToReps {
    public static void main(String[] args) {

	Scanner sc = new Scanner(System.in);
    // int test = sc.nextInt();
    int test = 1;
	while (test > 0) {
            test--;

            // int k = sc.nextInt();
            int k = 3;

            // String s = sc.next().trim();
            // String s = "abcdefghi";
            String s = "abcabcabc";

            int start = 0;
            int end = 0;

            HashMap<String, Integer> map = new HashMap<>();
            int max = Integer.MIN_VALUE;
            while (end <= s.length()) {

                if (end - start >= k) {

                    String sub = s.substring(start, end);

                    int value = map.getOrDefault(sub, 0);
                    if (max < ++value) {
                        max = value;
                    }
                    map.put(sub, value);

                    start++;
                } else {
                    end++;
                }

            }

            int lengthNeedToReplace = s.length() - max * k;

            int cost = lengthNeedToReplace * k;
            System.out.println(cost);
	}

	sc.close();
    }
}
