class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        gen = pow(3,i)
        while(gen <= n):
            if gen == n:
                return True
            i += 1
            gen = pow(3,i)
        return False