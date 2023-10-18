class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        gen = pow(4, i)
        while(gen <= n):
            if gen == n:
                return True
            i += 1
            gen = pow(4, i)
        return False