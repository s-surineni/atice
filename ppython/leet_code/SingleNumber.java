public class SingleNumber {
    public static void main(String[] args) {
        SingleNumber ns = new SingleNumber();
        int[] nums = {1,2,1,3,2,5};
        for (int i : ns.singleNumber(nums)) {
            System.out.println(i);
        }
    }
    public int[] singleNumber(int[] nums) {
        if (nums == null || nums.length < 2 || nums.length % 2 != 0) {
            throw new IllegalArgumentException("Invalid Input");
        }

        int aXORb = 0;
        for (int n : nums) {
            aXORb ^= n;
        }
        System.out.println(-aXORb);
        int rightSetBit = aXORb & -aXORb;
        int a = 0;
        for (int n : nums) {
            if ((n & rightSetBit) != 0) {
                a ^= n;
            }
        }

        return new int[] {a, aXORb ^ a};
    }
}