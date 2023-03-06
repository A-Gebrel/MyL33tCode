class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = list(range(1,4001))
        for i in arr:
            missing.remove(i)
        return missing[k-1]