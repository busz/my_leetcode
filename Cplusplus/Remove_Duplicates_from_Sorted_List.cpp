/*
Leetcode : Remove_Duplicates_from_Sorted_List.cpp

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
*/

#include <iostream>

using namespace std;

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
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode *node = head;
        if(head == NULL)
            return head;
        while(node != NULL)
        {
            while(node->next != NULL && node->next->val == node->val )
            {
                node->next = node->next->next;
            }
            node = node->next;
            
        }
        return head;
    }
};

