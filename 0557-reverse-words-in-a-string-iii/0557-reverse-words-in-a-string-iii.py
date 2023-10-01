class Solution:
    def reverseWords(self, s: str) -> str:
        newS = []
        lst = s.split(" ")
        print(lst)
        for i in lst:
            newS.append(i[::-1])
        res = ''
        for i in range(len(newS)):
            res += newS[i]
            if(i != len(newS)-1):
                res += " "
        return res