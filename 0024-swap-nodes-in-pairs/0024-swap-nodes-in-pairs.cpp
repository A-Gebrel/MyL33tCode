/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* curr;
        curr = head;
        while(curr != NULL && curr->next != NULL)
        {
            ListNode* first = curr;
            ListNode* second = curr->next;
            int temp;
            temp = first->val;
            first->val = second->val;
            second->val = temp;
            curr = curr->next;
            curr = curr->next;
        }
        return head;
    }
};