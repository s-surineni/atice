class Solution {

    int[][][] memo = new int[27][27][300];

    public int minimumDistance(String word) {
        return minDist(word, 0, null, null);
    }

    private int minDist(String word, int pos, Character c1, Character c2) {
        if (pos >= word.length())
            return 0;
        int idx1 = c1 == null ? 0 : c1 - 'A' + 1;
        int idx2 = c2 == null ? 0 : c2 - 'A' + 1;
        if (memo[idx1][idx2][pos] == 0) {
            memo[idx1][idx2][pos] = Math.min(
                    getDist(c1, word.charAt(pos)) + minDist(word, pos + 1, word.charAt(pos), c2),
                    getDist(c2, word.charAt(pos)) + minDist(word, pos + 1, c1, word.charAt(pos)));
        }
        return memo[idx1][idx2][pos];
    }

    private int getDist(Character c1, Character c2) {
        if (c1 == null || c2 == null)
            return 0;
        int d1 = c1 - 'A', d2 = c2 - 'A';
        int x1 = d1 / 6, y1 = d1 % 6;
        int x2 = d2 / 6, y2 = d2 % 6;
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

}

class DistToTypeWord {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.minimumDistance("CAKE");
    }
}