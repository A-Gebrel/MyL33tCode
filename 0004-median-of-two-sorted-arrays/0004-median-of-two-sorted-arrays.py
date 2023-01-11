class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        for i in nums1:
            nums3.append(i)
        for i in nums2:
            nums3.append(i)
        nums3.sort()
        size = len(nums3)
        if(size % 2 == 0):
            print(nums3[(size/2)-1])
            print(nums3[(size/2)])
            median = (nums3[(size/2)-1] + nums3[(size/2)])
            return float(median)/2
        else:
            median = nums3[size/2]
            return median
            