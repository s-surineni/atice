class HeightChecker {
    public int heightChecker(int[] heights) {
        int[] heightToFreq = new int[101];
        
        for (int height : heights) {
            heightToFreq[height]++;
        }
        
        int result = 0;
        int curHeight = 0;
        
        for (int i = 0; i < heights.length; i++) {
            while (heightToFreq[curHeight] == 0) {
                curHeight++;
            }
            
            if (curHeight != heights[i]) {
                result++;
            }
            heightToFreq[curHeight]--;
        }
        
        return result;
    }

    public static void main(String[] args) {
        HeightChecker hc = new HeightChecker();
        int[] heights = {1, 1, 4, 2, 1, 3};
        // for (int i = 0; i < heights.length; i++) {
        //     heights[i] = Integer.parseInt(args[i]);
        // }
        hc.heightChecker(heights);
    }
}
