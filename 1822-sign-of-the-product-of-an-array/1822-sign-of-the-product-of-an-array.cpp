class Solution {
public:
    int arraySign(vector<int>& nums) {
        if(nums[0] == 0)
            return 0;
        int product = nums[0];
        for(int i = 1; i<nums.size(); i++)
        {
            if(nums[i] == 0)
                return 0;
            else
                if(nums[i] > 0)
                    product *= 1;
                else
                    product *= -1;
        }
        if(product > 0)
            return 1;
        else
            return -1;
    }
};