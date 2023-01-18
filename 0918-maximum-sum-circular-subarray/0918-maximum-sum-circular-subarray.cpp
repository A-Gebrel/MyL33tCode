class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int max_sum = nums[0];
        int curr_max = nums[0];
        int total_sum = nums[0];
        int min_sum = nums[0];
        int curr_min = nums[0];
        int max_element = nums[0];
        bool all_negative = true;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > 0) all_negative = false;
            curr_max = max(nums[i], curr_max + nums[i]);
            max_sum = max(max_sum, curr_max);
            curr_min = min(nums[i], curr_min + nums[i]);
            min_sum = min(min_sum, curr_min);
            total_sum += nums[i];
            max_element = max(max_element, nums[i]);
        }
        if (all_negative) return max_element;
        return max(max_sum, total_sum - min_sum);
    }
};