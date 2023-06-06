class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if(len(arr) == 2):
            return True
        arr2 = list(arr)
        arr2.sort()
        diff = abs(arr2[0] - arr2[1])
        for i in range(2, len(arr2)):
            if(abs(arr2[i-1] - arr2[i]) != diff):
                print(diff, abs(arr2[i-1] - arr2[i]) )
                return False
            else:
                i += 1
        return True
            