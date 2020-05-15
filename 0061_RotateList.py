# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Special case: List is empty
        if head == None:
            return None
        # Special case: List has only one entry
        elif head.next == None:
            return head
        
        
        # Finding last node and counting size
        size = 1
        p,q = head, head
        
        while q.next != None:
            size += 1
            q = q.next
        
        # Closing loop
        q.next = head
        
        # Special case: k is greater than size
        k %= size
        
        # Sever chain at right location
        for i in range(size - k):
            q = q.next
            
        p = q.next
        q.next = None
        
        return p