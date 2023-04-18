class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        i, j = 0, 0
        while(len(word1) != 0):
            word3 += word1[0]
            word1 = word1[1:]
            if(len(word2) != 0):
                word3 += word2[0]
                word2 = word2[1:]
        if(len(word2) != 0):
            word3 += word2
        return word3
            