# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Handle edge cases
        if k > length:
            return head

        if k == length - k + 1:
            return head

        curr = head
        for i in range(1, k):
            curr = curr.next
        first_node = curr

        curr = head
        for i in range(1, length - k + 1):
            curr = curr.next
        second_node = curr

        # Swap the values of the two nodes
        first_node.val, second_node.val = second_node.val, first_node.val
        return head