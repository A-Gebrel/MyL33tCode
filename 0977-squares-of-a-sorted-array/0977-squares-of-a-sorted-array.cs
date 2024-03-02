public class Solution {
    public int[] SortedSquares(int[] nums) {
        int[] newSort = new int[nums.Length];
        for(int i=0; i< nums.Length; i++)
        {
            newSort[i] = nums[i]*nums[i];
        }
        Array.Sort(newSort);
        return newSort;
    }
}