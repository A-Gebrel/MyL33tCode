class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        map<int, int> numbers;
        for(int i=0; i<nums.size(); i++)
        {
            if(numbers.count(nums[i]) == 0)
                numbers.insert({nums[i], 1});
            else
                return nums[i];
        }
        return -1;
    }
};