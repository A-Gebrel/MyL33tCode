class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[],[]]
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                pass
            else:
                res[0].append(i)
        for i in nums2:
            if i in nums1:
                pass
            else:
                res[1].append(i)
        return res