/*
Leetcode : Remove_Nth_Node_From_End_of_List.cpp

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
*/

#include <iostream>

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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if(head->next == NULL and n==1)
        {
            delete head;
            head = NULL;
            return head;
        }
        ListNode *fast = head ;
        ListNode *slow = head;
        for(int i = 0 ; i < n + 1 ; i++)
        {
            if(fast == NULL)
            {
                ListNode *newHead = head->next;
                delete head;
                return newHead;
            }
                
            fast = fast->next;
        }
        while(fast)
        {
            fast = fast->next;
            slow = slow->next;
        }
        ListNode *node = slow->next;
        delete node;
        slow->next = slow->next->next;
        
        return head;
    }
};
