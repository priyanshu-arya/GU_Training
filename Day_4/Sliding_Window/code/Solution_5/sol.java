package Day_4.Sliding_Window.code.Solution_5;
public class sol {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;

        int left = 0, result = 0;
        long product = 1;

        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];

            while (product >= k) {
                product /= nums[left++];
            }

            result += (right - left + 1);
        }

        return result;
    }
}
