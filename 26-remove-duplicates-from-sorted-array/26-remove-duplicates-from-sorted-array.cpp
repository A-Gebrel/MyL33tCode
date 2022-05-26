class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int num2[nums.size()];
        int dupCount = 0;
        int index = 0;
        int tempNo = nums[0];
        num2[index++] = tempNo;
        for(int i=1; i<nums.size(); i++)
        {
            if(nums[i] == tempNo)
            {
                nums[i] = -101;
                dupCount++;
                num2[index] = nums[i];
                index++;
            }
            else
            {
                num2[index] = nums[i];
                index++;
                tempNo = nums[i];
            }
        }
        index = 0;
        for(int i=0; i<nums.size(); i++)
        {
            if(num2[i] == -101)
            {
                // do nothing lol
            }
            else
            {
                nums[index] = num2[i];
                index++;
            }
        }
        return nums.size()-dupCount;
    }
};