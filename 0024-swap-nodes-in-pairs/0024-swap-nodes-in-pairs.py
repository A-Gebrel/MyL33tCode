# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while(curr):
            first = curr
            if(curr.next):
                second = curr.next
            else:
                break
            if(second):
                first.val, second.val = second.val, first.val
            curr = curr.next
            curr = curr.next
        return head