class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        gen = pow(2,i)
        while(gen <= n):
            if gen == n:
                return True
            i += 1
            gen = pow(2,i)
        return False