public class Solution {
    public int[] FindErrorNums(int[] nums) {
        List<int> firstList = new List<int>();
        firstList.AddRange(nums);
        
        int[] errorNums = new int[2];
        for(int i=1; i<=nums.Length; i++)
        {
            if(firstList.FindAll(x => x==i).Count >= 2)
            {
                errorNums[0] = i;
                break;
            }
        }
        
        for(int i=1; i<=nums.Length; i++)
        {
            if(!firstList.Contains(i))
            {
                errorNums[1] = i;
                break;
            }
        }
        return errorNums;
    }
}