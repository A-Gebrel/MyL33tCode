class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = len(nums)//2
        cpy = list(set(nums))
        # res = []
        for i in cpy:
            if(nums.count(i) > freq):
                return i
        return False