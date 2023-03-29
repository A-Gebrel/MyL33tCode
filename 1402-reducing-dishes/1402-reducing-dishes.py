class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satcpy = list(satisfaction)
        satcpy.sort()
        satcpy = satcpy[::-1]
        check = 0
        red = 0
        for i in range(len(satcpy)):
            check += satcpy[i]
            if check < 0:
                break
            red += check
        return red