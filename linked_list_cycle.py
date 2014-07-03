'''
Created on 2014-2-25


leetcode : linked list cycle 

Problem : 

Given a linked list , detecrmine if it has a cycle in it 
Follow up : 

Can you solve it without using extra space ?

Solve : 

@author: xqk
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self , x ):
        self.val = x
        self.next = None
        
class Solution:
    # @param head , a ListNode
    # @return a boolean
    def hasCycle(self , head ):
        if head == None or head.next == None:
            return False
        if head.next == head:
            return True
        fast = head
        slow = head
        f = False
        while fast.next:
            if (slow == fast and f):
                return True
            elif(fast.next.next):
                f= True
                fast = fast.next.next
                slow = slow.next
            else:
                return False
        return False
        
        
        
        
        
        
        #using extra space  Time Limit Exceeded
        
        #=======================================================================
        # if head == None or head.next == None:
        #     return True
        # q = [head]
        # node = head.next
        # while node.next != None and node not in q:
        #     q.append(node)
        #     node = node.next 
        # if node.next == None:
        #     return True
        # else:
        #     return False
        #=======================================================================
head = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
head.next = h2
h2.next = h3
h3.next = h4
h4.next = h2

test = Solution()
print test.hasCycle(head)