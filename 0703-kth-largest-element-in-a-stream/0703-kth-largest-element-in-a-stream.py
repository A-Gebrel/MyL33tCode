class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.inums = []
        self.inums.extend(nums)
        self.kth = k
        self.inums.sort()
    def add(self, val: int) -> int:
        self.inums.append(val)
        self.inums.sort()
        return self.inums[-self.kth]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)