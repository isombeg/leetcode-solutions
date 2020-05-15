# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def flat(node):
    #base case: node is a leaf
    if node.left == None and node.right == None:
        return node
    
    if(node.right != None):
        a = flat(node.right)
    else:
        a = node
    if(node.left != None):
        b = flat(node.left)
    else:
        b = node
        return a
    
    b.right = node.right
    node.right = node.left
    node.left = None
    
    return a if not(a is node) else b
    
        

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root != None):
            flat(root)
        
        