class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        res = [i + extraCandies >= largest for i in candies]
        return res