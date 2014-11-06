/*
Leetcode : Merge_Two_Sorted_Lists.cpp

Merge two sorted linked lists and return it as a new list. The new list

should be made by splicing together the nodes of the first two lists.
*/


#include <iostream>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if(l1 == NULL )
            return l2;
        if(l2 == NULL)
            return l1;

        ListNode *head = NULL;
        ListNode *start = NULL;
        if(l1->val < l2->val)
        {
            head = l1;
            l1 = l1->next;
        }
        else
        {
            head = l2;
            l2 = l2->next;
        }
        start = head;

        while (l1 != NULL && l2 != NULL)
        {
            if(l1->val < l2->val)
            {
                start->next = l1;
                l1=l1->next;
            }
            else
            {
                start->next = l2;
                l2=l2->next;
            }
            start = start->next;
        }

        if (l1 != NULL)
            start->next = l1;
        if(l2 != NULL)
            start->next = l2;
        return head;
    }
};
int main()
{
    ListNode *l1 = new ListNode(2);
    ListNode *l2 = new ListNode(1);
    Solution test = Solution();
    ListNode * result = test.mergeTwoLists(l1,l2);
}
