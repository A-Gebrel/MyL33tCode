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
    ListNode* swapNodes(ListNode* head, int k) 
    {
        int length = 0;
        ListNode* curr = head;
        while (curr) {
            length++;
            curr = curr->next;
        }

        if (k > length || k <= 0) {
            return head;
        }

        if (k == length - k + 1) {
            return head;
        }

        curr = head;
        for (int i = 1; i < k; i++) {
            curr = curr->next;
        }
        ListNode* first_node = curr;

        curr = head;
        for (int i = 1; i < length - k + 1; i++) {
            curr = curr->next;
        }
        ListNode* second_node = curr;

        swap(first_node->val, second_node->val);

        return head;
    }
};