class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if(target in letters):
            pass
        else:
            letters.append(target)
        letters = list(set(letters))
        letters.sort()
        index = letters.index(target)
        if(letters[-1] == target):
            return letters[0]
        if(index == len(letters)-1):
            return letters[0]
        else:
            return letters[index+1]