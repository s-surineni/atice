import java.util.Queue;
import java.util.PriorityQueue;


class TroopsEvacuation {
    public static void main(String[] args) {
        // int[] nums1 = {8, 12, 7, 3};
        // int[] nums2 = {8, 7, 9, 10, 3};
        int[] nums2 = {1, 2, 3, 4};
        // System.out.println(getMaxSum(nums1));
        System.out.println(getMaxSum(nums2));
    }

    private static int getMaxSum(int[] nums) {
        Queue<Integer> maxHeap = new PriorityQueue<Integer>((a, b)->b-a);
        for(int n : nums)
            maxHeap.offer(n);
        int res = 0;
        while(maxHeap.size() > 1) {
            int cur = maxHeap.poll();
            int next = maxHeap.poll();
            res += cur;
            if(next + 1 != cur)
                maxHeap.offer(next);
        }
        if(!maxHeap.isEmpty())
            res += maxHeap.poll();
        return res;
    }
}
