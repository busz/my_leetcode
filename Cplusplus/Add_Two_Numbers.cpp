/*
Leetcode : Add_Two_Numbers.cpp

You are given two linked lists representing two

non-negative numbers. The digits are stored in

reverse order and each of their nodes contain

a single digit. Add the two numbers and return

it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {

        ListNode *l3 = new ListNode(l2->val + l1->val );
        int carry = l3->val/10;
        l3->val = l3->val%10;

        ListNode *sum = l3;
        l1 = l1->next;
        l2 = l2->next;
        while(l1 && l2)
        {

            l3->next = new ListNode(l2->val + l1->val + carry);
            l3 = l3->next;
            carry = l3->val/10;
            l3->val = l3->val%10;
            l2 = l2->next;
            l1 = l1->next;
        }
        if(l1)
        {
            while(l1 != NULL)
            {
                l3->next = new ListNode(l1->val + carry);
                l3 = l3->next;
                carry = l3->val/10;
                l3->val = l3->val%10;
                l1 = l1->next;
            }
        }
        else if(l2)
        {
            while(l2 != NULL)
            {
                l3->next = new ListNode(l2->val + carry);
                l3 = l3->next;
                carry = l3->val/10;
                l3->val = l3->val%10;
                l2 = l2->next;
            }

        }


        if(carry)
            l3->next = new ListNode(carry);


        return sum;
    }
};

int main()
{
    Solution test = Solution();

    ListNode *l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    ListNode *l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);
    ListNode *result = test.addTwoNumbers(l1 , l2);
    while(result != NULL)
    {
        cout<<result->val<<endl;
        result = result->next;
    }
    return 0;
}
