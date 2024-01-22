public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int duplicate = -1;
        int missing = -1;
        List<int> firstList = new List<int>();
        firstList.AddRange(nums);
        
        int[] errorNums = new int[2];
        for(int i=1; i<=nums.Length; i++)
        {
            if(firstList.FindAll(x => x==i).Count >= 2)
            {
                duplicate = i;
                break;
            }
        }
        
        for(int i=1; i<=nums.Length; i++)
        {
            if(!firstList.Contains(i))
            {
                missing = i;
                break;
            }
        }
        
        errorNums[0] = duplicate;
        errorNums[1] = missing;
        return errorNums;
    }
}