/*
Leetcode : Partition_List.cpp

Given a linked list and a value x, partition it such

that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the

nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

*/

#include <iostream>
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        if(!head || ! head->next )
            return head;

        ListNode *traverse = head;
        ListNode *rt = NULL;
        ListNode *rtStart = NULL;
        ListNode *lt = NULL;
        ListNode *ltStart = NULL;
        while(traverse)
        {
            if(traverse->val < x)
            {
                ListNode *tmp = traverse;
                traverse = traverse->next;
                if(!ltStart)
                {
                    ltStart = tmp;
                    lt = tmp;
                }
                else
                {
                    lt->next = tmp;
                    lt = lt->next;
                }
            }
            else
            {
                ListNode *tmp = traverse;
                traverse = traverse->next;
                
                if(!rtStart)
                {
                    rtStart = tmp;
                    rt = tmp;
                }
                else
                {
                    rt->next = tmp;
                    rt = rt->next;
                }
            }
        }
        
        
        if(lt)
            lt->next = rtStart;
        else
            ltStart = rtStart;
        return ltStart;
    }
};

int main()
{
    Solution test = Solution();
    ListNode *head = new ListNode(1);
    head->next = new ListNode(1);
    ListNode *result = test.partition(head , 2);
    while(result!=NULL)
    {
        cout<<result->val<<endl;
        result = result->next;
    }


}
