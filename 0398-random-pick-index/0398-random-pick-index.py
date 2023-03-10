class Solution:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for i, num in enumerate(nums):
            if(num not in self.dic):
                self.dic[num] = [i]
            else:
                self.dic[num].append(i)

    def pick(self, target: int) -> int:
        dic = self.dic[target]
        result = random.choice(dic)
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)