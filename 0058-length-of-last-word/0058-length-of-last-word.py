class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        scpy = s.split(" ")
        scpy = list(filter(None, scpy))
        print(scpy)
        return len(scpy[-1])