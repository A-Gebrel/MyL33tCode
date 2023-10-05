class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)//3
        cpy = list(set(nums))
        res = []
        for i in cpy:
            if(nums.count(i) > freq):
                res.append(i)
        return res