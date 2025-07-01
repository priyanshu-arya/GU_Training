package Day_4.Sliding_Window.code.Solution_4;

public class sol {
    public int longestOnes(int[] nums, int k) {
        int left = 0, right = 0, maxLen = 0, zeros = 0;

        while (right < nums.length) {
            if (nums[right] == 0) zeros++;

            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
            right++;
        }

        return maxLen;
    }
}
