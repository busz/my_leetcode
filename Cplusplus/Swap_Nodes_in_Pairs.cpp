/*
leetcode : Swap_Nodes_in_Pairs.cpp
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values 

in the list, only nodes itself can be changed.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        if(head == NULL or head->next == NULL)
            return head;
        ListNode *pre = NULL;
        ListNode *fast = head->next;
        ListNode *slow = head;
        head = fast;
        while(1)
        {
            ListNode *next = fast->next;
            fast->next = slow;
            slow->next = next;
            if(pre)
            {
                pre->next = fast;
            }
            
            if(slow->next == NULL or slow->next->next == NULL)
                break;
            else
            {
                pre = slow;
                slow = slow->next;
                fast = fast->next->next->next;
            }
        }
        return head;
    }
};
