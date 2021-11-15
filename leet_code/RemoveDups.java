class Solution {
    public String removeDuplicates(String s) {
        int i = 0, n = s.length();
        char[] res = s.toCharArray();
        for (int j = 0; j < n; ++j, ++i) {
            res[i] = res[j];
            System.out.println(res);
            if (i > 0 && res[i - 1] == res[i]) // count = 2
                i -= 2;
        }
        String rest = new String(res, 0, i);
        return rest;
    }
}

public class RemoveDups {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.removeDuplicates("abbaca"));
    }
}