class Solution:
# simple solution by looping and checking for positive/negatives
    def arraySign(self, nums: List[int]) -> int:
        if(nums[0] == 0):
            return 0
        product = nums[0]
        nums = nums[1::]
        for i in nums:
            if i == 0:
                return 0
            product *= i;
        if product > 0:
            return 1
        else:
            return -1
        