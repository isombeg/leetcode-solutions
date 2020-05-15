# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        hashtab = dict()
        
        while p != None:
            if p in hashtab:
                return True
            else:
                hashtab[p] = True
                p = p.next
        return False
            