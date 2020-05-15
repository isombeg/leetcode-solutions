"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def conn(n):
    #Base case
    if n.left == None and n.right == None:
        n.next= None
        return n
    
    a = conn(n.left)
    a.next = n.right
    b = n.right
    
    while a.right != None:
        a = a.right
        b = b.left
        a.next = b
    
    conn(n.right)
    n.next = None
    return n

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(root != None):
            conn(root)
        
        return root