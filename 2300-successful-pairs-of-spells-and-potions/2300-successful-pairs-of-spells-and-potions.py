class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        good = []
        for i in spells:
            count = 0
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if i * potions[mid] < success:
                    left = mid + 1
                else:
                    count = len(potions) - mid
                    right = mid - 1
            good.append(count)
        return good