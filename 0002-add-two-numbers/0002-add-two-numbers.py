# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        while(l1):
            num1 += str(l1.val)
            l1 = l1.next
        while(l2):
            num2 += str(l2.val)
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3 = int(num1) + int(num2)
        num3 = str(num3)
        l3 = list(num3)
        for x,y in enumerate(num3):
            if x == 0:
                l3[x] = ListNode(val=int(y), next = None)
            else:
                l3[x] = ListNode(val=int(y), next=l3[x-1])
        return l3[len(l3)-1]