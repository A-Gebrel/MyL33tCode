class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        
        int tempcons = 0;
        int cons = tempcons;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i] == 1)
            {
                tempcons++;
            }
            else
            {
                tempcons = 0;
            }
            if(cons < tempcons)
            {
                cons = tempcons;
            }
        }
        return cons;
    }
};