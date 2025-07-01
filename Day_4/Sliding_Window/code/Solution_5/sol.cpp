class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;

        int left = 0, result = 0;
        long long product = 1;

        for (int right = 0; right < nums.size(); ++right) {
            product *= nums[right];

            while (product >= k) {
                product /= nums[left++];
            }

            result += (right - left + 1);
        }

        return result;
    }
};
