"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        queueA, queueB = list(), list()
        queueA.append(root)
        
        while len(queueA) > 0:
            while len(queueA) > 0:
                holder = queueA.pop(0)
                
                if holder.left != None:
                    queueB.append(holder.left)
                if holder.right != None:
                    queueB.append(holder.right)
                
                if len(queueA) > 0:
                    holder.next = queueA[0]
                else:
                    holder.next = None
            
            queueB, queueA = queueA, queueB
            
        return root