class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = ""
        totalcount = 0
        while(len(s) !=0):
            if(s[0] in curr):
                curr = ""
                totalcount += 1
                curr += s[0]
            else:
                curr += s[0]
            s = s[1:]
        if(len(curr) != 0):
            totalcount += 1
        return totalcount