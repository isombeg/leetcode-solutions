# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Special case: List is empty
        if head == None:
            return None
        
        p, count = head, 0
        hashtab = dict()
        hashtab[p] = count
        while p != None:
            if p.next in hashtab:
                return p.next
            else:
                count += 1
                hashtab[p.next] = count
                p = p.next
                
        return None