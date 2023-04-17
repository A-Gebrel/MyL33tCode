class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        # print(largest)
        res = []
        for i in candies:
            if(i+extraCandies >= largest):
                res.append(True)
            else:
                res.append(False)
        return res