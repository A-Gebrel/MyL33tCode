class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        good = []
        for i in spells:
            count = len(potions) - bisect.bisect_left(potions, (success + i - 1) // i)
            good.append(count)
        return good