/*

Leetcode : Linked_List_Cycle.cpp

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
*/



// Definition for singly-linked list.
 struct ListNode {
     int val;
    ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL )
            return false;
        ListNode *fast = head->next;
        ListNode *slow = head;
        while(fast && fast->next)
        {
            if(fast == slow)
                return true;
            else
            {
                slow = slow->next;
                fast = fast->next->next;
            }
        }
        return false;
    }
};
