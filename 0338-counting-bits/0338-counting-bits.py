class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n+1):
            num = str(bin(i))
            res.append(num.count('1'))
        return res