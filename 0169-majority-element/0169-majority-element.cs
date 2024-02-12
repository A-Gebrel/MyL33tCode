public class Solution {
    public int MajorityElement(int[] nums) {
        if(nums.Length == 1)
            return nums[0];
        int freq = nums.Length/2;
        Dictionary<int, int> myDic = new Dictionary<int, int>();
        for(int i=0; i<nums.Length; i++)
        {
            if(!myDic.TryAdd(nums[i], 1))
            {
                myDic[nums[i]] = myDic[nums[i]]+1;
                if(myDic[nums[i]] > freq)
                    return nums[i];
            }
        }
        return -1;

    }
}