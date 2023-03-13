class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        numcpy = x
        reverse = 0
        isNegative = False
        if numcpy < 0:
            numcpy *= -1
            isNegative = True
        while(numcpy >= 10):
            to_add = numcpy % 10
            numcpy = numcpy // 10
            reverse = reverse * 10 + to_add
        reverse = reverse * 10 + (numcpy % 10)
        if reverse > 4294967295:
            return 0
        if reverse >= 2147483651:
            return 0
        if isNegative:
            return reverse * -1
        return reverse