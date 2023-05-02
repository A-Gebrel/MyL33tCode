class Solution:
# simple solution by looping and checking for positive/negatives
# another idea would be sort the array then
# A) check if the array has 0, if so return 0
# B) if not, check the count of positive (or negative) numbers
# C) mathematically decide whether it would return 1 or -1
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
        