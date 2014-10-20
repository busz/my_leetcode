/*
Leetcode : Copy_List_with_Random_Pointer.cpp

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

*/

/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head == NULL)
            return NULL;
        RandomListNode *next = head;
        while(next)
        {
            RandomListNode *tmp = next;
            next =  next->next;
            RandomListNode *newNode = new RandomListNode(tmp->label);
            newNode->next = next;
            tmp->next = newNode;
        }
        next = head;
       
        while(next)
        {
            RandomListNode *tmp = next;
            if(tmp->random)
                tmp->next->random = tmp->random->next;
            next = next->next->next;
        }
        next = head;
        RandomListNode *newHead = head->next;
        RandomListNode *newNext = NULL;
        while(next)
        {
            if(newNext)
            {
                newNext->next = next->next;
                newNext = newNext->next;
            }
            else
                newNext = next->next;
            next->next = next->next->next;
            next = next->next;
        }
        return newHead;
    }
};
