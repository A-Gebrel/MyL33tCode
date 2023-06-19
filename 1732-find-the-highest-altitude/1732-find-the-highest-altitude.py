class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = []
        alt.append(0)
        for i in range(1, len(gain)):
            alt.append(alt[i-1] + (gain[i-1]))
        alt.append(alt[-1] + (gain[-1]))
        return max(alt)