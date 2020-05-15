"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashmap = dict() # map original nodes to deep copies
        
        # Special case: List is empty
        if head == None:
            return None
        # Special case: List has one node
        if head.next == None:
            newHead = Node(head.val, None, None)
            if head.random == head:
                newHead.random = newHead
            return newHead
        
        p,q,newHead = head, head.next, Node(head.val, None, None)
        a = newHead
        # Construct singly-linked list and record corresponding nodes
        while q != None:
            a.next = Node(q.val, None, None)
            hashmap[p] = a
            a = a.next
            p = p.next
            q = q.next
        hashmap[p] = a
        
        # Make the random connections
        p,a = head, newHead
        while p != None:
            if p.random == None:
                a.random = None
            else:
                a.random = hashmap[p.random]
            a = a.next
            p = p.next
            
        return newHead